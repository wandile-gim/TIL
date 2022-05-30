# Permissions

인증과 스로틀링과 함께 permission은 요청이 허가될 것인지 거부될 것인지 결정을 도와준다. 

Permission checking은 항상 View의 시작 전에 시작되는데 request.user와 request.auth에 있는 인증 정보로 request정보가 허가될 수 있는지 판단한다. 

View의 메인 body가 실행되기 전 listed된 각각의 permission이 체크되고 permission이 실패한다면 exception이 발생되고 view의 main body가 실행되지 않는 컨셉이다.



## 장고에서 제공하는 기본적인 Permission Class

### AllowAny

**regardless of if the request was authenticated or unauthenticated**.

인증, 비인증의 여부와 상관없이 허가된다.

### IsAuthenticated

any unauthenticated user에 대해 허가를 거부한다.

### IsAdminUser

 `user.is_staff` 속성이 True인 사용자에 한해서 허가한다.

### IsAuthenticatedOrReadOnly

인증되지 않은 사용자는"safe" methods인  `GET`, `HEAD` or `OPTIONS`에 대해서 읽기가 허가되고 authenticated users에 대해서 모든 접근을 허가한다.

### Custom Permissions

Permission에 대해서 사용자가 요구사항에 맞춰 커스텀할 수 있다. 

Custom Persmission Class를 정의하기 위해서는 아래의 조건이 필요하다.

- BasePermission를 Override

- `.has_permission(self, request, view)`
- `.has_object_permission(self, request, view, obj)`

- 위 두 메서드중 하나 혹은 모두를 재정의해야하고 has_object_permission의 경우 has_permission을 통과한 경우 사용될 수 있다.

인스턴스 수준 검사를 실행하려면 `.check_object_permissions(request, obj)`가 명시적으로 호출해야 하는데,

has_permission의 처리는 Generic View에서는 Default로 `.check_object_permissions(request, obj)`이 자동 처리되지만 

Function Based View에서는 PermissionDenied가 발생 되었을 경우 명시적으로 개체 권한을 확인해야 하는 차이가 있다.

#### Example

has_permission이 처리 되었을 경우 아래와 같이 Object에 대해 Permission 기능을 작성할 수 있다.

```python
class OwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user
```

review_user가 obj의 속성임을 가정했을때 GET으로 요청되는 request에는 읽기가 허용되고 댓글을 작성한 사용자라면 요청하는 사용자가 작성자인지 object를 검사해야한다.  

safe_method가 아닌 post, put, delete등의 요청은  request user가 review_user와 동일하다면 접근에 대한 permission을 승인한다.



아래는 들어오는 요청의 IP 주소를 차단 목록과 비교하여 해당 IP가 차단된 경우 요청을 거부하는 권한 클래스의 예시이다.

```python
from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
        return not blocked
```



들어오는 모든 요청에 대해 실행되는 전역 권한뿐만 아니라 특정 개체 인스턴스에 영향을 미치는 작업에 대해서만 실행되는 object-level permissions을 만들 수도 있다.

```python
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
```

Generic View는 object level permissions을 확인하지만 Custom View를 작성하는 경우 object level permission을 직접 확인해야 한다. self.check_object_permissions(request, obj) 개체 인스턴스가 있으면 뷰에서 호출 할 수 있다.

이 호출은 object level permission이 실패하면 `APIException` 을 발생시키고 그렇지 않으면 단순히 반환한다.

또한 Generic View에서는 단일 모델 인스턴스를 retreive view하기 위한 object-level permissions만 확인하지만, list view의 개체 수준 필터링이 필요한 경우 query-set을 별도로 필터링해야 한다.



참조 : https://www.django-rest-framework.org/api-guide/permissions/ drf공식 문서 