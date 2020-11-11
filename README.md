# MOBILE NOTIFICATION
**TỔNG QUAN** 
- Ứng dụng được xây dựng với mục đích giúp *khảo sát khách hàng về chất lượng dịch vụ tại các cửa hàng*. Khi có một khách hàng sử dụng dịch vụ của cửa hàng, nhân viên thu ngân sẽ tạo phiếu khảo sát, Khi vừa tạo phiếu khảo sát, màn hình Ipad sẽ chuyển hướng đến trang có chứa phiếu khảo sát.
------------------
**CHI TIẾT:**
-   Ứng dụng được xây dựng bằng flutter sử dụng ngôn ngữ dart, có thể dể dàng build ra ứng dụng cung cấp cho thiết bị android và IOS. Dựa vào cơ chế nhận notification phía firebase nên ứng dụng đảm bảo đầy đủ tính toàn vẹn(mỗi device sẽ có 1 token device riêng).
-   Phân phối: Gói dữ liệu được lưu trữ thẳng xuống firebase firestore từ app winform(Sử dụng thư viện firebase google cloud), khi có thay đổi trong firebase firestore, firebase function(API) sẽ tiếp nhận và gửi gói dữ liệu(chứa đường dẫn đến phiếu khảo sát) đến thiết bị thông qua fcm-token. Phía flutter lắng nghe, khi có 1 notification mới đến(thực chất là url), Hàm sẽ chuyển hướng đến website với đường dẫn đích là url vừa tiếp nhận thông qua thư viện inwebappview.
-   Các chức năng phụ: 
    -	Tự động điều chỉnh độ sang của màn hình sau 5p không sử dụng.
    -	Quản lý thiết bị.
    -	Màn hình bảo vệ phần quản lý thiết bị(mật khẩu 123333).
    -	Quay lại màn hình chờ
    -	Ghi đè khi có một even mới.

------------------------------------------

**FOR DEVELOPER:**
YÊU CẦU:
MACOS(64-bit)
-	OS:  10.15.
-	XCODE: version 12.(yêu cầu >40GB trống trong máy để cài đặt được xcode 12)
FLUTTER: 2.8GB trống.
-------------------
**LIBRARY**
- Flutter App (IOS) https://flutter.dev/docs/deployment/ios
- Dart.
- Flutter_inappwebview: web . https://pub.dev/packages/flutter_inappwebview
- Shared_preferences: Lưu trữ tên thiết bị vào đĩa cứng device. https://pub.dev/packages/shared_preferences
- Rich_alert: Tạo các dialog Alert. https://pub.dev/packages/rich_alert
- Passcode_screen: tạo màn hình bảo mật khi vào cấu hình tên thiết bị. https://pub.dev/packages/passcode_screen
- Vibration: rung. https://pub.dev/packages/vibration
- Wakelock: Giữ device luôn sang. https://pub.dev/packages/wakelock
- Screen: tùy chỉnh độ sáng https://pub.dev/packages/screen
- Firebase_analytics,Firebase_mesaging,Firebasecore,cloud_firestore: kết nối đến firebase để lưu trữ token, kiểm tra tên device. https://pub.dev/packages/cloud_firestore

------------------------------------------

DEMO
# Màn hình khoá phần quản lý thiết bị.
![màn hình khoá](https://drive.google.com/uc?export=view&id=1cZU2HWMae6_4R_nBeWaFr24KtCBudhc8)


# Màn hình quản lý thiết bị.
![màn hình quản lý thiết bị](https://drive.google.com/uc?export=view&id=1LPSIWpJZnt24MobfxIhgsnPnMGjJ99HD)


# Rich alert.
![Rich alert](https://drive.google.com/uc?export=view&id=1GKGQnfmTSVMQINLq4u7_0NKmkCTex85m)


# Màn hình web được nhúng vào ứng dụng.
![Chuyển hướng đến web nhúng](https://drive.google.com/uc?export=view&id=1H2bNI0vnen1OMGakM-EXNb7oijPN2TKn)

