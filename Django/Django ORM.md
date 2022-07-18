# Django ORM

장고 공식 문서를 정리한 내용.

### Select_related()

- `select_related`(**fields)*



#### 쿼리 부스터 역할

외래키 관계를 따라 `QuerySet` 을 반환한다. 복잡한 쿼리를 생성하는 쿼리 부스터 역할을 하고 추가적인 쿼리 히트 없이 외래키 관계의 데이터베이스 쿼리가 필요하지 않는다. 

```python
# Hits the database.
e = Entry.objects.get(id=5)

# Hits the database again to get the related Blog object.
b = e.blog
```

 `select_related` lookup:

```python
# Hits the database.
e = Entry.objects.select_related('blog').get(id=5)

# 데이터베이스에 쿼리를 발생시키지 않는다. e.blog는 이미 이전 쿼리에 의해 저장되어있기 때
b = e.blog
```



또한 select_related()는 어느 쿼리셋에도 적용할 수 있다.

```python
from django.utils import timezone

# Find all the blogs with entries scheduled to be published in the future.
blogs = set()

for e in Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog'):
    # select_related()을 사용하지 않으면, 'blog'의 모든 엔트리를 반복하면서 데이터베이스에 쿼리를 발생시킨다. 
    blogs.add(e.blog)
```

filter()와 select_related()의 체이닝 순서는 중요하지 않다. 아래의 쿼리셋도 동일하다.

```python
Entry.objects.filter(pub_date__gt=timezone.now()).select_related('blog')
Entry.objects.select_related('blog').filter(pub_date__gt=timezone.now())
```



#### 예시 모델

```python
from django.db import models

class City(models.Model):
    # ...
    pass

class Person(models.Model):
    # ...
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Book(models.Model):
    # ...
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
```



Book.objects.select_related('author__hometown').get(id=4)는 Person연관과 City연관을 캐싱한다.

그렇기 때문에 아래와 같이 데이터 베이스를 추가로 히트시키지 않아도 되기 때문에 비용을 절약할 수 있다.

```python
b = Book.objects.select_related('author__hometown').get(id=4)
p = b.author		#Doesn't hit the database.
c = b.hometown	#Doesn't hit the database.

# select_related()를 사용하지 않운 경우
b = Book.objects.get(id=4)  # Hits the database.
p = b.author         # Hits the database.
c = p.hometown       # Hits the database.
```



##### Arguments 없이 select_related()를 호출

쿼리가 복잡하고 실제로 필요한 데이터보다 더 많은 데이터를 반환하기 때문에 권장되진 않지만 찾을 수 있는 모든 non-null인 외래키를 찾아준다.



##### select_related()는 다른 메서드와 유사한 방식으로 동작한다. 

```python
# 예를 들어
select_related('foo', 'bar') 
select_related('foo').select_related('bar') 
# 는 동일하다.
```

