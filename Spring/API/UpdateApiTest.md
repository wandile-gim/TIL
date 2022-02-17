## UpdateApi 테스트 코드작성

스프링에서 지원하는 편리한 메소드들 덕분에 테스트를 편리하게 처리할 수 있다.

PostApiContorller에서 PutMapping을 /api/v1/posts{id}로 받았기 때문에 먼저 도메인에 엔티티를 세이브 해주고 반환받은 Posts타입에서 id를 가져와서 url에 받는다.

여기서 편리한 기능은 TestRestTemplate에서 exchange메서드로 url,통신타입,적용할 엔티티를 받아 내부적으로 put을 요청해 ResponseEntity를 반환해준다는 것이다. 

그럼 반환받은 엔티티의 정보를 비교만해주면 테스트를 통과함을 알 수 있다.

```
@Test
    public void Posts_Updated() throws Exception{

        Posts posts = postsRepository.save(Posts.builder()
                .title("title")
                .content("content")
                .author("author")
                .build());

        Long updatedId = posts.getId();
        String expectedTitle = "title2";
        String expectedContent = "content2";

        PostsUpdateRequestDto dto = PostsUpdateRequestDto.builder()
                .title(expectedTitle)
                .content(expectedContent)
                .build();

        String url = "http://localhost:" + port + "/api/v1/posts" + updatedId;

        HttpEntity<PostsUpdateRequestDto> reponseEntity = new
                HttpEntity<>(dto);
        //when
        ResponseEntity<Long> responseEntity = testRestTemplate
                .exchange(url, HttpMethod.PUT, reponseEntity, Long.class);

        //then
        assertThat(responseEntity.getStatusCode())
                .isEqualTo(HttpStatus.OK);
        assertThat(responseEntity.getBody())
                .isGreaterThan(0L);

        List<Posts> postsList = postsRepository.findAll();
        assertThat(postsList.get(0).getTitle())
                .isEqualTo(expectedTitle);
        assertThat(postsList.get(0).getContent())
                .isEqualTo(expectedContent);
```



### 느낀점

확실히 테스트 코드를 작성하면서 클라이언트에서 기능이 구현되는 것을 확인 하는 것과 실제 로직 속에서 도메인, 서비스, DTO, Controller, View 의 역할이 구분되어 원리에 대해서 더 가까이 이해할 수 있었다.

MVC패턴의 내부 동작 과정들에 맞춰 서버를 구축할 수 있을 것 같다.



### 배운것

HttpEntity를 살펴보면 Represents an HTTP request or response entity, consisting of headers and body.

DTO객체를 헤더와 바디로 구성된 리스폰스 엔티티로 나타내준다. 그러면 **exchange**에서 바로 url에 매핑된 요청을 이 

dto데이터를 담은 HttpEntity로 put해준다는 것이다.
