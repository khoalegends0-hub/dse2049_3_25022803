# LTXLDL — pilot lab 01, 02, 03

Mỗi sinh viên có một **private repo riêng trong `uet-iai-notebook-labs-2026`**, chứa cả ba lab.
Đây là bộ pilot để thử quy trình nộp/chấm, chưa phải điểm chính thức của môn học.

| File | Nội dung | Điểm máy tối đa | Phần giảng viên |
|---|---|---:|---:|
| [lab-01.ipynb](lab-01.ipynb) | Notebook, trạng thái, đọc dữ liệu và quy trình AI | 40 | 60 |
| [lab-02.ipynb](lab-02.ipynb) | Python, CSV, làm sạch và tổng hợp | 80 | 20 |
| [lab-03.ipynb](lab-03.ipynb) | NumPy, masks, axis, phân vị và argsort | 80 | 20 |

## Làm bài

1. Mở notebook bằng Colab hoặc Jupyter. Điền cell TODO và phần trả lời Markdown.
2. Chạy public checks ngay trong notebook; trước khi nộp dùng Restart & Run all.
3. Lưu file về đúng tên và vị trí gốc của repo. Lưu trên Drive chưa phải nộp GitHub.

Không có GitHub Actions ở repo sinh viên. Public checks phục vụ tự kiểm tra;
private grader chấm độc lập, không đọc bảng PUBLIC_RESULTS hay output lưu sẵn để lấy điểm.

Giữ nguyên cell ID, tên hàm/biến và hợp đồng input/output. Có thể viết helper trong chính cell bài làm;
grader không chạy những cell helper mới nằm rải rác ngoài cell đó. Các câu được chấm độc lập với đầu vào riêng.
Các import chuẩn `csv`, `json`, `numpy as np`, `pandas as pd` và hàm `trung_vi` được cung cấp khi phù hợp.
Phần markdown do giảng viên đọc. Các bài E của lab 02–03 vẫn là mở rộng tùy chọn, không làm giảm điểm Q.

## Môi trường và dữ liệu

Khuyến nghị Python 3.12. Nếu chạy local:

```bash
python -m pip install -r requirements.txt
python -m ipykernel install --user --name ltxldl --display-name "LTXLDL"
```

Chọn kernel LTXLDL trong Jupyter/VS Code. Colab có sẵn nhiều thư viện; chỉ cài khi import chưa hoạt động.

Notebook mở mặc định bằng 6 dòng giả lập để thử quy trình; không suy rộng kết quả thành kết luận về Santiago.
Có thể dùng snapshot Santiago 2026-06-29 theo hướng dẫn notebook. Q2 lab 01 chấp nhận câu trả lời đọc bảng
cho bộ 6 dòng hoặc snapshot 18.534 dòng đã nêu trong đề. Các hàm khác phải tính từ input, không ghi cứng số.
Private grader không tải URL từ notebook và không chạy API bên ngoài.

## Nộp một lab

Repo phải được giảng viên đăng ký trước. Ví dụ nộp lab 02 lần đầu trên branch `main`:

```bash
git add lab-02.ipynb
git commit -m "Submit lab 02 attempt 1"
git push origin main
git tag submit/lab-02/v1
git push origin submit/lab-02/v1
```

Tag tương ứng của lab 01 và 03 là `submit/lab-01/v1`, `submit/lab-03/v1`.
Pilot hiện hỗ trợ v1, v2, v3 cho từng lab. Sửa bài phải tạo commit mới và tag lần tiếp theo;
không di chuyển/force-push tag đã nộp. Commit/push không có tag chưa được xem là bài nộp tự động.

## Xem kết quả

Grader quét **20:00 thứ Bảy, giờ Việt Nam**; giảng viên có thể chạy thủ công để thử ngay.
Giờ bắt đầu thực tế có thể trễ do GitHub xếp hàng.

Mở commit mà tag trỏ tới → xem status `private-grader/lab-01`, `private-grader/lab-02` hoặc
`private-grader/lab-03`. Ví dụ `Auto 70/80; manual 20 pending` nghĩa là máy đã chấm 70/80,
20 điểm còn chờ giảng viên; đây chưa phải điểm cuối cùng. Status xanh chỉ xác nhận các mục Q tự động đã qua.
Không cần vào tab Actions ở repo sinh viên. Link Details dẫn đến grader private, chỉ giảng viên xem được.

Nếu đã nộp đúng tag nhưng chưa có status, gửi giảng viên tên repo, lab, tag và commit SHA.
