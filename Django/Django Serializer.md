# Django Serializer

Serializer는 model의 Serialization과 form의 validation 기능을 제공해주기 때문에 지원되는 두 기능과 같은 것으로 보여진다. 

## 메모리 내부 vs 메모리 외부

프로그램을 실행하면 메모리의 내부에서 진행된다.

메모리의 데이터를 File, DB, Network로 보내려면 내부, 외부의 환경이 다르기 때문에 데이터 형식을 맞출 필요가 있다.

###  복원시 정보 유지

Serialize된 데이터를 복원시 그 정보를 유지해야한다.



Serializer의 두가지 역할 직렬화, 역직렬화에 대해서 Comment 테이블에 대해서 실험을 진행한다.

### serialize

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

##### serialize 의 DataFlow

Instance,

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

 

