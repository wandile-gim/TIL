# [DRF] filter_queryset

DRF의 Generic APIView에서 구현되는 filter_queryset 메서드의 구현 코드에 달린 주석을 보면, 

```py
 """
    Given a queryset, filter it with whichever filter backend is in use.
    You are unlikely to want to override this method, although you may need
    to call it either from a list view, or from a custom `get_object`
    method if you want to apply the configured filtering backend to the
    default queryset.
"""
```

filter backend가 사용되는 곳에 적용되는 쿼리셋으로 볼 수 있는데, 쿼리의 집합이 지정된 경우에 사용중인 필터 백엔드로 필터링하는 사용의 목적이 있다.

구성된 필터링 백엔드를 에 적용하려는 경우 filter_queryset method를 재정의하여 View에서 필터링된 데이터를 제공한다.



View에 정의된 filter_queryset()은 1개의 파라미터(quertset)를 받지만 filter-backends에 정의된 filter_queryset()은 request, queryset, view를 파라미터로 받는다 



## filter-backend란?

filter-backend는 복잡한 룩업 및 기타 항목으로 쿼리 세트를 필터링하는 데 도움이 되는 클래스이다.

drf는 몇가지의 built-in backendf를 제공한다. django의 django-filter 패키지를 사용해 더 향상된 필터링 기능을 구현할 수 있다. 



DjangoFilterBackend클래스 내부를 살펴보자 

```python
def filter_queryset(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if filterset is None:
            return queryset

        if not filterset.is_valid() and self.raise_exception:
            raise utils.translate_validation(filterset.errors)
        return filterset.qs
```

내부 로직에서 filterset을 가져와 쿼리를 만들어내기위해

Get_filterset -> 쿼리 파라미터와, 쿼리셋, request정보를 가지고 get_filterset_class를 호출한다. 



```python
 def get_filterset_class(self, view, queryset=None):
        """
        Return the `FilterSet` class used to filter the queryset.
        """
        filterset_class = getattr(view, 'filterset_class', None)
        filterset_fields = getattr(view, 'filterset_fields', None)	

##아래는 생략..
     return filterset_class

        if filterset_fields and queryset is not None:
            MetaBase = getattr(self.filterset_base, 'Meta', object)

            class AutoFilterSet(self.filterset_base):
                class Meta(MetaBase):
                    model = queryset.model
                    fields = filterset_fields

            return AutoFilterSet

        return None
```

view에서 filterset_class와 filterset_fields를 가져와 쿼리셋 모델을 반환해준다. 반환된 쿼리셋 모델은 filter_queryset으로 반환되어 

None일 경우 queryset을 반환하고 유효하다면 filter가 적용된 qs을 반환해준다. 



이로써 Custom generic filtering을 만들어 필터링된 새 쿼리셋을 만들어 클라이언트가 검색 및 필터링을 수행할 수 있을뿐만 아니라 generic filter 백엔드는 특정 요청이나 사용자에게 표시되어야 하는 객체를 제한하는데 유용하다. 아래는 간단한 해당 예시이다. 

```python
class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
```



View에서 get_queryset()을 사용하여 물론 같은 결과를 만들어 낼 수 있지만 GenericView에서 filter-backend를 사용해 더 간결하고 쉽게 추가할 수 있는 장점이 있다.

