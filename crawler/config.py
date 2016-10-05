class Fb_config():
    def __init__(self, target):
        self.target = target
        # TODO : 항상 타겟이 이렇게 세팅되지 않음. profile.php?id=<int> 이렇게 붙기도 함
        # 이럴때는 sk=likes 이렇게 붙음.
        # maps에서 이미 다 출력했는데 아무 메시지가 나오지 않을 때도 있음.
        self.base_url = "https://www.facebook.com/" + target

        # TODO: 너무 self 많이 썼는데 사용하지 않고 할 수 있는 방법 찾기
        self.TIMELINE_CLASS = "_1w_m"

        self.LIKE_CLASS = "ul.uiList._4-sn._5k35._620._509-._4ki"
        self.MAP_CLASS = "ul.uiList._620._14b9._509-._4ki"
        self.EVENT_CLASS = "ul.uiList._4-sn._509-._4ki"
        self.GROUP_CLASS = "ul.uiList._4-sn._509-._4ki"

        self.MOVIE_CLASS = "ul.uiList._620._14b9._5pst._5psx._509-._4ki"
        self.BOOK_CLASS = "ul.uiList._620._14b9._5pst._5psx._509-._4ki"

        # "<target> 추가 정보"
        self.STOP_CLASS = ".mbm._5vf.sectionHeader._4khu"

        self.NOT_FOUND_CLASS = "div._4-y-"
        self.NOT_FOUND_TEXT = "없음"

        self.LOGIN_FAILED_TEXT = "Facebook에 로그인"
        # TODO: profile 아직 긁는 기능 없음
        """
        정보
        - 개요
        - 경력 및 학력
        - 거주했던 장소
        - 연락처 및 기본 정보
        - 가족 및 결혼 연애 상태
        - <target>에 대한 자세한 소개
        - 중요 이벤트
        """

        self.url_list = {
            # "timeline": ["타임라인", self.base_url,self.TIMELINE_CLASS],
            # 사용자 정보 항목
            # "profile": ["프로필", self.base_url + '/about'],
            "like": ["좋아요", self.base_url + '/likes', self.LIKE_CLASS],
            "map": ["체크인", self.base_url + '/map', self.MAP_CLASS],
            "event": ["이벤트", self.base_url + '/events', self.EVENT_CLASS],
            "group": ["그룹", self.base_url + '/groups', self.GROUP_CLASS],
            # movie & book are watched event.
            "movie": ["영화", self.base_url + '/video_movies_watch', self.MOVIE_CLASS],
            "book": ["책", self.base_url + '/books_read', self.BOOK_CLASS]
        }
