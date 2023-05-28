# automatical_capture_macOS

### auto PDF Capture program
> 라이브러리
- pynput | keyboard handling
    - [공식문서](https://pynput.readthedocs.io/en/latest/keyboard.html)

> 코드 프로세스
- 사전 작업
    - shift + command + 5를 누르고, PDF의 캡쳐가 필요한 부분의 프레임을 맞춰줍니다. -> 이때, 프레임은 다음 페이지를 넘겼을 때도 전체가 나오게 유지 해야 합니다. 본인 기준 (전체화면 + 105% + 90% 축소)
    - 불필요한 옵션을 제거 합니다. -> 미리보기 썸네일 체크 해제, 마우스 포인터 보기 체크 해제
    - 위 단계에서 보이는 다른 위치를 설정 하여 스크린샷을 생성할 폴더를 지정합니다.

    
- 프로그램 실행 프로세스
    - 반복 페이지 개 수 만큼
        1. Mac os의 캡쳐 단축키를 누릅니다.
        2. 캡쳐 단축키를 누릅니다.
        3. 다음 화면을 넘깁니다.


- 후처리 작업
    - 저장이 완료 된 폴더에 접근 하여, command + a로 스크린샷 파일을 전체 선택 한 후, 빠른 동작 -> PDF 생성을 클릭하면 의도한 PDF를 캡쳐 하여 본인만의 PDF 생성을 반자동화를 이용 할 수 있습니다.

### 주의 할 점
- 이 프로그램은 단축키를 이용하여 반복 하는 작업이기 때문에, 초기 프레임 설정을 기가 막히게 해주셔야 합니다. 다음 버튼을 눌렀을 때 화면이 초기화 되지 않고 설정한 프레임이 유지 된다면 이 프로그램을 작동 했을 땐 원하는 캡쳐기능을 이용 할 수 있습니다.


### 실행
- git clone
- install library
    ```
    pip3 install -r requirments.txt
    ```
- 입력 인자 값
    - range 범위 : PDF 전체 페이지 개 수
    - sleep 시간 : 코드를 실행 한 후 얼마 뒤 캡쳐 프로세스가 실행 될 지
    
- python run
    - system arguments help command
        ```
        optional arguments:
        -h, --help            show this help message and exit
        -t TIME, --time TIME  Run process after wait time >> default =
                                1
        -p PAGE, --page PAGE  Count of pages in PDF viewr. this is
                                most parameter
        ```

    e.g                    
    ```
    python3 save_capture.py -t 5 -p 1
    ```
