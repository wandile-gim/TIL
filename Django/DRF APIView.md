# Django Rest Framework

## DRF Class 상속도

#### DRF를 공부하기 시작할 때 ViewSet의 구현만으로 기본적인 CRUD 구현이 된다. 

DRF의 상속도를 보면 

![image-20220414205412908](/Users/wonjae/Library/Application Support/typora-user-images/image-20220414205412908.png)



최상위에 View클래스가 있고 View클래스를 상속 받아 APIView, APIView를 상속받아 GenericAPIView를 만들었고

Mixin클래스들을 조합해 ViewSet들을 만들었다.  

![image-20220414205706976](/Users/wonjae/Library/Application Support/typora-user-images/image-20220414205706976.png)

GenericAPIView들에 대해 CRUD API들(CreateAPIView, RetrieveAPIView, UpadateAPIView, DestroyAPIView)은 각각 Mixin들을 조합해 만들어졌다.

정리하면. 

| CRUD   | GenericAPIView  | RestAPI       |
| ------ | --------------- | ------------- |
| Crete  | CreateAPIView   | POST          |
| Read   | ListAPIView     | GET           |
|        | RetrieveAPIView | GET           |
| Update | UpadateAPIView  | UPDATE, PATCH |
| Delete | DestroyAPIView  | DELETE        |

그리고 5개의 APIView들을 모아 ModelViewSet이 만들어졌다. 



## APIView Class

GenericAPIView에 대해 정리해볼 때

먼저 제네릭 뷰의 실행 흐름을 보면.

#### Generic View Flow 

1. data from DB

2. serialize

* ListAPIView
  * PostSerializer(instance=, many=True)
    * *** DB에서 가져온 데이터를 instance에 대입 many True는 여러개의 시리얼라이징***

* RetrieveAPIView
  * PostSerializer(instance=, many=False)
    * *** DB에서 가져온 데이터를 instance에 대입 many False는 한 개의 시리얼라이징***

3. response
4. 

읽기 역할을 하는 ListAPIView와 RetrieveAPIView의 차이점은. 

먼저 List는 DB에서 가져온 데이터를 인스턴스에 대입해서 여러개의 데이터에 대해 시리얼 라이징 해준다.

반대로 Retrieve는 단일의 데이터에 대해 시리얼라이징 해준다는 차이가 있다.



그렇다면 ModelViewSet을 사용하는 것과 나뉘어진 Generic View를 사용하는 것에 대한 차이가 뭘까??



**GenericViewSet**은 GenericAPIView에서 상속되지만 기본 작업의 구현을 제공하지 않음. get_object, get_queryset만 있으면 됨

**ModelViewSet** 은 GenericAPIView에서 상속되며 다양한 작업에 대한 구현을 포함. 즉, list, retrieve, create, update 또는 destroy 같은 기본 작업을 구현할 필요가 없고,이들을 오버라이딩하고 고유한 목록 또는 고유한 메소드를 구현할 수 있다는 점이다.