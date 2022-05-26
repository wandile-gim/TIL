# Django Serializer

참조 https://www.django-rest-framework.org/api-guide/relations/#nested-relationships (Drf공식 문서)

Serializer는 model의 Serialization과 form의 validation과 같은 기본적인 기능 외에도 추가적인 정말 용이한 기능을 제공하고있다.



## 메모리 내부 vs 메모리 외부

프로그램을 실행하면 메모리의 내부에서 진행된다.

메모리의 데이터를 File, DB, Network로 보내려면 내부, 외부의 환경이 다르기 때문에 데이터 형식을 맞출 필요가 있다.

###  복원시 정보 유지

Serialize된 데이터를 복원시 그 정보를 유지해야한다.

Serializer의 두가지 역할 직렬화, 역직렬화에 대해서 Comment 테이블에 대해서 실험을 진행한다.

### Serialize

```python
c0 = Commment.object.all()[0]
sr = CommentSerializer(instance = c0)
sr.data
#{'id': 1, 'content': 'ㅋㅋㅋㅋㅋㅋ첫 댓글이당', 'create_dt': '2022-04-18T14:31:14.311661+09:00', 'update_dt': '2022-04-18T14:31:14.311745+09:00', 'post': 1}
data0 = sr.data
type(data0)
# class ... ReturnDict

json0 = JsonRenderer().render(data0)
type(json0)
#bytes로 변환된다.
```



##### Serialize 의 DataFlow

Instance

Serializer(instance)

dict

json data

response



serialize는 변환된 데이터를 서버측에서 전송하는 역할을 하고 클라이언트의 요청에 응답한다.

데이터를 instance화 시키고 serializer를 통해 dict형식의 데이터로 변환하고 이를 json포맷으로 응답한다.

read operation을 수행하고 GET메소드와 호환된다.



### deserialize

```python
from io import BytesIO

ddata0 = JSONParser().parse(BytesIO(json0))
type(ddata0)
# dict

dsr = CommentSerializer(data=ddata0)
dsr.is_valid()
#True
dsr.errors
#{}

dsr.validate_data

instance = Comment(**dsr.validate_data)
instance.save()
```

##### deserialize의 DataFlow

json data,

dict

Serializer(data=xxx)

is_valid(), validated_data

instance

Save



json포맷의 데이터를 dictionary로 변환하고 변환된 데이터를 serializer로 역직렬화를 수행한다.

deserialized된 데이터를 검증해서 사용해야하기 때문에 is_valid()를 통과해야하고

통과된 데이터는 validated_data에 저장된다.

validated_data는 저장될 수 있는 형식이므로 instance가 되고 저장한다.

write operation을 수행하고 POST, UPDATE, DELETE, PATCH 메소드와 호환된다.



## Validation

### Field level validation

```python
def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
```

Serializer에 명시된 field에 validation check는 Serializer클래스에 valiate_foo(self, data)메서드를 만들어 사용한다.

validate_(field name)

유효성을 통과하지 못할 경우 에러를 발생 시킨다. 발생된 에러는 View에서 is_valid하지 않는다면 serializer.errors를 사용해 확인할 수 있다.

### Object level validation

Serializer 클래스에 valiate를 정의해 Object가 가진 값을 확인 가능하다. Serializer가 가진 필드는 key값이 되어 value를 참조할 수 있다. 

```python
def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
```

 

## API Reference

공식 문서에 나와있는 예제 모델이다. 공식문서에서 이 모델을 바탕으로 Serializer가 제공하는 기능을 설명하는데 정말 강력한 기능을 제공한다는 느낌을 많이 받았다..



```python
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
```



### StringRelatedField

`StringRelatedField` 는   `__str__` 메서드를 사용하는 타깃의 연관관계를 표현하는데 사용된다. 예를들어, 

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

아래는 연관 관계에 있는 모델에 정의된  `__str__`메서드 이다.

```python
  def __str__(self):
        return '%d: %s' % (self.order, self.title)
```

tracks에서 `__str__`이 적용된 형태로 데이터를 제공해준다.

```json
{
    'album_name': 'Things We Lost In The Fire',
    'artist': 'Low',
    'tracks': [
        '1: Sunflower',
        '2: Whitetail',
        '3: Dinosaur Act',
        ...
    ]
}
```

to-many 연관관계에 적용하려면  `many` 를 True로 적용해야한다.



### SlugRelatedField

`SlugRelatedField`는 연관관계에 있는 타겟의 필드를 표현하는데 사용된다. 예를들어, 

```python
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']
```

연관관계에 있는 track테이블의 필드중 `slug_field`에 지정한 필드는 아래와 같이 표현된다. 

```json
{
    'album_name': 'Dear John',
    'artist': 'Loney Dear',
    'tracks': [
        'Airport Surroundings',
        'Everything Turns to You',
        'I Was Only Going Out',
        ...
    ]
}
```

StringRelatedField는 연관 테이블의 `__str__`메서드를 타겟으로 한다면 SlugRelatedField는 테이블의 속성을 타겟으로 표현해준다.



**Arguments**:

- `slug_field` - The field on the target that should be used to represent it. This should be a field that uniquely identifies any given instance. For example, `username`. **required**

- `queryset` - The queryset used for model instance lookups when validating the field input. Relationships must either set a queryset explicitly, or set `read_only=True`.

- `many` - If applied to a to-many relationship, you should set this argument to `True`.

- `allow_null` - If set to `True`, the field will accept values of `None` or the empty string for nullable relationships. Defaults to `False`.

  

공식문서에서 참조한 SlugRelatedField의 Arguments들이다. slugfield는 소개한내용 그대로이고 many역시 to-many연관 관계를 표현하기 위한 속성이다. 

allow_null의 경우 기본값이 False인데, True로 설정할 경우 nullable한 관계에서 None이나 empty한 데이터를 허용해주는 속성이다.



