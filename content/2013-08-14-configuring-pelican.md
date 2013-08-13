Title: Pelican 설정하기
Tags: pelican
Category: blogging
Slug: configuring-pelican
Summary: Pelican을 설정하는 방법.


## Markdown extension

설정 파일을 수정한다. 추가 가능한 확장과 사용법은 [여기](http://pythonhosted.org/Markdown/extensions/)에서
확인 가능하다. 참고로 다음의 codehilite와 extra는 default이므로 추가하고 싶은 확장이 없으면
MD\_EXTENSIONS은 따로 설정하지 않아도 된다. 그러나 추가하고 싶은 것이 있을 때 그것만 적으면
default에 있던 것은 없어지므로 default와 추가하고 싶은 것을 같이 적어야 할 것이다.

	:::python
	MD_EXTENSIONS = [
	    'codehilite(css_class=highlight)',
	    'extra',
	]
