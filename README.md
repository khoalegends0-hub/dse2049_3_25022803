# Notebook labs — pilot

Private repository cho bài nộp thử nghiệm của môn học. Notebook `lab01.ipynb`
có implementation mẫu đúng để kiểm thử hệ thống; bản bài tập chính thức sẽ được
giảng viên thay bằng starter trước khi phát cho sinh viên.

## Chạy bài và public tests

Dùng Python 3.11:

```bash
python -m pip install -r requirements-ci.txt
python -m ipykernel install --user --name python3 --display-name "Python 3"
python -m pytest -q --tb=short --maxfail=0 tests_public
```

## Nộp bài

Lưu notebook, commit, rồi push lên `main`. Mỗi lần muốn nộp lab01, dùng tag mới:

```bash
git add lab01.ipynb
git commit -m "Complete lab01"
git push origin main
git tag submit/lab01/v1
git push origin submit/lab01/v1
```

Các lần sửa tiếp theo dùng `v2`, `v3`; không đổi hoặc xóa tag đã nộp.
Public tests trên GitHub chạy khi push submit tag hoặc khi chạy workflow thủ công.
Giảng viên cần bật chấm hidden cho repo của bạn; chỉ tạo tag chưa tự cấp quyền
cho hệ thống chấm. Với pilot tự động, giảng viên chạy workflow Organization pilot
ở private grader và sinh viên chỉ thấy commit status `pilot-hidden/lab01`.

Repository này được tạo từ template độc lập. Nội dung và test của giảng viên
không được phát trong repository bài nộp.
