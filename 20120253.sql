USE QLSV
GO

--4.1
SELECT * 
FROM SinhVien sv 
WHERE sv.ma in 
(SELECT sv2.ma 
FROM (SinhVien sv2 join Lop l on l.ma = sv2.maLop) join Khoa k on k.ma = l.maKhoa, KhoaHoc kh 
WHERE k.tenKhoa = N'Công nghệ thông tin' and kh.namBatDau = '2002' and kh.namKetThuc = '2006')

--4.2
SELECT sv.ma, sv.hoTen, sv.namSinh 
FROM SinhVien sv join lop l on l.ma = sv.maLop join KhoaHoc kh on kh.ma = l.maKhoaHoc
WHERE (kh.namBatDau - sv.namSinh) < 18

--4.3
SELECT * 
FROM SinhVien sv join lop l on l.ma = sv.maLop
WHERE l.maKhoa = 'CNTT' and l.maKhoaHoc = 'K2002' and N'Cấu trúc dữ liệu 1' not in 
(SELECT mh.tenMonHoc 
FROM MonHoc mh join KetQua kq on kq.maMonHoc = mh.ma 
WHERE kq.maSinhVien = sv.ma)

--4.4
SELECT * 
FROM SinhVien sv join KetQua kq on kq.maSinhVien = sv.ma join MonHoc mh on mh.ma = kq.maMonHoc
WHERE kq.diem < 5 and 1 = ALL(SELECT kq2.lanThi FROM KetQua kq2 WHERE kq2.maSinhVien = sv.ma) and mh.tenMonHoc = N'Cấu trúc dữ liệu 1'

--4.5
SELECT l.ma, l.maKhoaHoc, ct.tenChuongTrinh, COUNT(sv.ma) as N'Số sinh viên của lớp'
FROM Lop l join ChuongTrinh ct on ct.ma = l.maChuongTrinh join SinhVien sv on sv.maLop = l.ma
GROUP BY l.ma, l.maKhoa, l.maKhoaHoc, ct.tenChuongTrinh
HAVING l.maKhoa = 'CNTT'

--4.6
SELECT AVG(kq.diem) as N'Điểm trung bình' 
FROM SinhVien sv join KetQua kq on kq.maSinhVien = sv.ma
WHERE kq.lanThi >= ALL(SELECT kq2.lanThi FROM KetQua kq2 WHERE kq2.maSinhVien = sv.ma and kq2.maMonHoc = kq.maMonHoc) and sv.ma = '0212003'

--5.1
--CREATE FUNCTION 