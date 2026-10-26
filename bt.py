"""
Bài tập: Lớp DienThoai
a. Xây dựng lớp DienThoai gồm: MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan
   và phương thức thongtindienthoai() hiển thị thông tin điện thoại.
b. Tạo 2 đối tượng điện thoại và gọi phương thức hiển thị.
"""


# a. Xây dựng lớp DienThoai
class DienThoai:
    """Lớp mô tả một chiếc điện thoại."""

    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        """Khởi tạo điện thoại với mã máy, tên máy, hãng, dung lượng pin (mAh) và giá bán (VNĐ)."""
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        """Hiển thị đầy đủ thông tin điện thoại."""
        print(f"Mã máy: {self.MaMay}")
        print(f"Tên máy: {self.TenMay}")
        print(f"Hãng sản xuất: {self.HangSanXuat}")
        print(f"Dung lượng pin: {self.DungLuongPin} mAh")
        print(f"Giá bán: {self.GiaBan:,} VNĐ")
        print("-" * 30)

    def __str__(self):
        """Chuỗi mô tả ngắn gọn khi dùng print(đối_tượng)."""
        return f"{self.TenMay} ({self.HangSanXuat}) - {self.GiaBan:,} VNĐ"


# b. Tạo 2 đối tượng và gọi phương thức
if __name__ == "__main__":
    dt1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    dt2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    dt1.thongtindienthoai()
    dt2.thongtindienthoai()

    # Dùng __str__
    print(dt1)
    print(dt2)