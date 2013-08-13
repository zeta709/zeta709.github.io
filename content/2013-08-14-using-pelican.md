Title: Pelican을 이용하여 블로그에 소스 코드 넣기
Tags: pelican
Category: blogging
Slug: insert-code-in-blog-using-pelican
Summary: Pelican을 이용하여 블로그에 소스 코드를 넣는 방법


## 소스 코드 넣기

Markdown을 사용하는 경우 다음과 같은 방법으로 소스 코드를 넣으면 된다.

	:::
	Normal text.

		:::identifier
		code here

우선 공백 줄을 넣고, 소스 코드는 전체적으로 한 단계씩 인덴트해준다.
참고: [Identifier의 목록](http://pygments.org/docs/lexers/)


## Gist 넣기

Gist를 사용하지 않아도 소스 코드를 넣고 구문 강조를 하는 것이 가능하다.
그러나 코드 조각을 gist에 저장하는 방법이 블로그 포스트에 텍스트 형태로
저장하는 방법보다 관리하기 편하기 때문에 어떤 코드들은 gist에 저장한 뒤
블로그에 넣는 방법을 사용하고 싶을 것이다.
포스트에 gist를 넣으려면
[pelican-gist](https://github.com/streeter/pelican-gist)
플러그인을 설치해야 한다. 다음과 같은 방법으로 설치하면 된다.
참고로 `(pelican)`은 virtualenv를 사용하는 상황을 나타낸 것이다.

	:::console
	(pelican)$ pip install pelican-gist

그리고 설정파일(`pelicanconf.py`)을 수정한다.

	:::python
	PLUGINS = [
	    'pelican_gist',
	]

이제 다음과 같은 방법으로 Gist를 넣을 수 있다.

	:::
	[gist:id=6220730,file=hello.py]

위 코드를 넣으면 다음과 같이 나온다.

[gist:id=6220730,file=hello.py]

정말 사소한 문제점이 있는데 그것은 다음과 같다.

* 사용자 이름을 지정하는 방법이 없다. 사용자 이름을 지정하지 않아도
  gist에 접근 가능하기 때문에 gist를 글에 넣는 것이 목적이라면
  크게 문제되는 것이 없다.
* 이 플러그인은 gist의 내용을 복사하여 `<noscript>` tag에 넣어둔다.
  만약 gist에 파일이 여러 개가 있는데, file을 지정하지 않고
  기본적인 방법
  (`<script src="https://gist.github.com/6220730.js"></script>`)
  을 이용하면 해당 gist 내의 모든 파일을 가져와서 출력한다.
  그러나 `<noscript>` tag에는 첫 번째 파일의 내용만 들어있다. 그 이유는
  gist의 파일 목록을 가져오는 것이 간단하지 않기 때문인 것으로 보인다.
  대부분의 경우 noscript tag는 사용되지 않을 것이므로, 이것은
  크게 문제되는 내용은 아닐 것 같다.
