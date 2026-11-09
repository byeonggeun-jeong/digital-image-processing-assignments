import plistlib
import base64


def decode_plist_data_and_save_to_file(file_path, output_file_path):
    try:
        # Plist 파일 열기
        with open(file_path, 'rb') as f:
            plist_data = plistlib.load(f)  # plistlib로 파일을 읽기

        # _payloadData라는 키를 찾고 해당 데이터를 Base64로 디코딩
        if "_payloadData" in plist_data:
            base64_data = plist_data["_payloadData"]

            # Base64로 인코딩된 데이터를 디코딩
            decoded_data = base64.b64decode(base64_data)

            # 디코딩된 데이터를 출력
            print("디코딩된 데이터 길이:", len(decoded_data))

            # 파일로 저장 (바이너리 형식으로 저장)
            with open(output_file_path, 'wb') as out_file:
                out_file.write(decoded_data)

            print(f"디코딩된 데이터를 파일로 저장했습니다: {output_file_path}")
        else:
            print("_payloadData 키가 존재하지 않습니다.")

    except Exception as e:
        print("Plist 파일 읽기 오류:", e)