#MOBILE NOTIFICATION
**TỔNG QUAN** 
Ứng dụng được xây dựng với mục khảo sát khách hàng về chất lượng dịch vụ tại các cửa hàng. Khi có một khách hàng sử dụng dịch vụ của cửa hàng, nhân viên thu ngân sẽ tạo phiếu khảo sát, Khi vừa tạo phiếu khảo sát, màn hình Ipad sẽ chuyển hướng đến trang có chứa phiếu khảo sát. 
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

- Flutter App (IOS)
- Dart
- Flutter_inappwebview:  Mô phỏng website. shared_preferences: Lưu trữ tên thiết bị vào đĩa cứng device.
- Rich_alert: Tạo các dialog Alert. passcode_screen: tạo màn hình bảo mật khi vào cấu hình tên thiết bị.
- Vibration: rung.
- Wakelock: Giữ device luôn sang.
- Screen: tùy chỉnh dộ sang
- Firebase_analytics,Firebase_mesaging,Firebasecore,cloud_firestore: kết nối đến firebase để lưu trữ token, kiểm - tra tên device.
- Điều hướng đến trang web theo đường dẫn vừa nhận
- Nguồn tham khảo:
- Inappwebview:
- https://pub.dev/packages/flutter_inappwebview
- shared_preferences:
- https://pub.dev/packages/shared_preferences
- passcode:screen: https://pub.dev/packages/passcode_screen

------------------------------------------

DEMO

