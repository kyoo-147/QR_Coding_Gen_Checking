# Dự án hệ thống nhận diện, truy xuất băng QR-Code cho nhân viên

## X_QR_System-ORP
X_QR_System-ORP là một hệ thống nhận diện và truy xuất các thông tin thời gian, và khởi động hệ thống cho nhân viên chỉ bằng mã QR-Code và có thể kết nối đến nhiều nền tảng lưu trữ

**Initial solution**

Thực hiện các quy trình kiểm soát nghiêm ngặt trong môi trường công ty, checking, tự động hóa. Tăng cường độ bảo mật và tính trung thực cho mọi môi trường. Có thể tương thích với các thiết bị công nghệ nhúng, nhằm phát triển và mở rộng tầm kiểm soát. Đặc biệt có thể kết nối đến các ứng dụng nằm trong hệ sinh thái của NaVin.

**Movation**
Giải pháp hệ thống nhận diện khuôn mặt đến từ NaVin là một giải pháp khá tốt, nhưng để gia tăng khả năng chính xác dành cho các hệ thống đạt được tính trung thực và bảo mật cao nhất. Đó là lí do X_QR_System_ORP ra đời nhằm gia tăng độ bảo mật tuyệt đối cho doanh nghiệp.

## Methodology
Đầu tiên, người dùng nhập khởi động giao diện chính của hệ thống. Theo tùy chọn, người dùng có thể nhập tên, thông tin và chức vụ của họ, để hệ thống có thể xử lí và tạo ra mã QR-Code. Sau đó, chương trình sẽ hoạt động và mã hóa lưu trữ dữ liệu QR-Code của bạn vào file data, tìm ra sai sót và đề xuất cải tiến. Lịch sử lưu trữ và các phản hồi, các thông tin đăng kí và các lần mở khóa, ngoài phản hồi được tạo, hệ thống tích hợp AI, dùng để nhận diện hành vi lạ trong việc sử dụng QR-Code để mở khóa, ví dụ như: Thử đi thử lại một mã QR-Code sai, nhận diện có hiện tượng lạ trong hành vi truy xuất, hệ thống sẽ thực hiện khóa cửa, và chờ sự xác nhận của các admin để xác nhận việc mở cửa. Quá trình này có thể được lặp lại vô thời hạn, tùy vào sự cài đặt của admin.
Sau đó, lịch sử tất cả sẽ được lưu trữ lại.

## Usage/requirements
Reqs:
`pip install requirements.txt`

Usage:
`python X_Main_X_ORP.py`