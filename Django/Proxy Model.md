# [Django] Multiple User Types with Proxy Model

## Proxy Model

:arrow_right:  모델 상속에 대한 방법들(abstract base class, multi-table inheritance, proxy model) 중 하나로 프록시 모델의 기반이 되는 원래 모델로 각기 다른 파이썬 behavior을 하는 모델들의 별칭을 가지며 동작하는 모델



예시를 두고 프록시 모델에 대해 알아보자

### Model fields

Base Model이 되는 `USER`모델이 있다.

- 이름
- 이메일
- 정체성(?)

의 필드를 가진다. 코드로 표현해보자면,



### Base Model

```python
class User(AbstractUser):
	class Types(models.TextChoices):
    STUDENT = "STUDENT", "Student"
		TEACHER = "TEACHER", "Teacher"
	type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.STUDENT)
  
  name = models.CharField(_('Name of User'), blank=True, max_length=255)
```

 User는 타입에 따라 정체성(?)이 선생님이 될 수도 있고, 학생이 될 수도 있게 또 각각의 역할에 맞게 모델 특성을 표현하고 싶을 때

공통된 User라는 모델을 바탕으로 각자의 정체성을 표현할 수 있다.



### Proxy Model

정체성을 나타내기 위해 Student와 Teacher를 정의해보자. 

**(Proxy Model은 Base Model의 필드 구조를 그대로 따라가기 때문에 필드 변경을 할 수가 없다.)**

```python
class Teacher(User):
	class Meta:
    proxy = True

class Student(User):
  class Meta:
    proxy = True
```



Teacher와 Student를 정의했다.

바로 shell에서 Teacher의 정체성을 가진 User를 생성해보자. 



```python
Student.objects.create(username = 'gildong', email = 'gildong@example.com', type = User.Types.STUDENT)
```



결과:

####  ![스크린샷 2022-11-02 오후 11.39.33](/Users/wonjae/Desktop/스크린샷 2022-11-02 오후 11.39.33.png)



Student를 생성했지만 Teacher에도 Student로 생성한 gildong이 조회되고 있다, 

이 시점에, 장고는 사용자에게 어떤 값을 컨트롤할 수 있는,  만들고 싶은, 대상을 원하기 때문에 정의를 해주어야한다. 



대상을 정의해주기 위해서 조회와 생성에서 각각 역할의 정체성에 알맞게 코드를 추가해주기 위해 `Manager`의 `get_queryset`을 오버라이딩하여 objects에 지정해준다.

```python
class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.TEACHER)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STUDENT)
```



![image-20221103004157863](/Users/wonjae/Library/Application Support/typora-user-images/image-20221103004157863.png)



이제 조회를 통해 각 type에 맞게 조회할  수 있게 되었으니, `save`를 마저 오버라이딩해준다. 

```python
class Teacher(User):
    ...
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.TEACHER


class Student(User):
		...
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STUDENT
```



또한,

모델을 상속 받는 방법으로 Proxy를 이용하면 원래 모델에 대해서만 테이블이 생성되어, **각기 다른 별칭을 가진 파이썬 Behavior를 만들 수가 있다는 장점**이 있다.

```python
class Teacher(User):
    ...
	def teaching(self):
    return 'blah blahhhh'
```

예를 들면 Teacher가 가진 teaching behavior처럼 모델의 정체성을 가지는 특정한 기능을 정의할 수도 있다는 것이다.

그렇기 때문에 Proxy한 방법의 상속이므로 모델 필드의 내용을 변경할 수가 없다는 단점을 가지고 있다.



학습내용 : two scoops of Django