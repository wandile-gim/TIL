# java.util.arrays



문자열이나, 객체의 데이터들을 정렬하기 위한 방법은 여러가지가 있다. 

그 중 java.util.Arrays 유틸리티 클래스를 사용해 배열을 쉽게 작업하는 방법은 해당 클래스의 sort()메서드를 활용해 쉽게 정렬 가능하다. 기본은 오름차순 정렬이다. 

자바에서 인스턴스를 서로 비교하는 클래스들은 Comaparable 인터페이스가 구현되어 있다.

Comaparable 인터페이스에서 compareTo 메서드가 오름차순 기준이기 때문이다.



오름차순 정렬 뿐아니라 정렬 조건을 다양하게 하려면 커스터마이징 해주면 된다.

Comparable인터페이스의 compareTo메서드를 원하는 조건으로 오버라이드 하거나,

Comparator를 구현한 클래스내에서 compare()메서드를 원하는 정렬조건으로 오버라이드 해주면 된다.



```
Integer[] intArr = new Integer[] {1,6,3,7,8};

Arrays.sort(intArr, new Comparator(){
	@Override
	public int compare(int o1, int o2){
		return o2.compareTo(o1);
	}
});
```

int형으로 타입을 규정해주지 않았는데 int, byte, char, short와 같은 타입은 primitive Type이기 때문에 클래스인 Wrapper클래스를 이용해야 한다.

혹은 이미 내림차순으로 구현되어있는 Comparator.reverseOrder()메서드를 반환해 주어도 된다.

```
String stringArr = new String[] {"a","b","c","d"};
Arrays.sort(stringArr,Comparator.reverseOrder());
```



### Stream API

배열이나 컬렉션을 스트림을 사용해 람다 표현식으로 간결한 표현 또한 가능하다.

```
String str = "RTGSDFG";

String sortedStr =  Stream.sort(str.split("")).sorted(Comparator.reverseOrder()).collect(Collectors.joining());
```

