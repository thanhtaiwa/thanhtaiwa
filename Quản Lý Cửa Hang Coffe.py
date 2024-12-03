import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

# danh sach dữ lieu
danh_sach_nhan_vien = []
drink_list = []
invoice_list = []

def main_window():
    root = tk.Tk()

    root.title("Hệ Thống Quản Lý Cửa Hàng Coffee")
    root.geometry('1100x900')


    button_frame = tk.Frame(root, width=300, height=700, bg="lightgray")
    button_frame.pack(side="left", fill="y")

    HienThi_frame = tk.Frame(root, width=700, height=600)
    HienThi_frame.pack(side="right", fill="both", expand=True)

    # Buttons

    tk.Button(button_frame, text="Nhân Viên", width=20, height=2, bg="#e7f5dc", command=lambda: hien_thi_nhan_vien(HienThi_frame)).pack(padx=20, pady=10, fill='x')
    tk.Button(button_frame, text="Danh Sách Thức Uống", width=20, height=2, bg="#cfe1b9", command=lambda: hien_thi_thuc_uong(HienThi_frame)).pack(padx=20, pady=10, fill='x')
    tk.Button(button_frame, text="Hoá Đơn", width=20, height=2, bg="#b6c99b", command=lambda: hien_thi_hoa_don(HienThi_frame)).pack(padx=20, pady=10, fill='x')
    tk.Button(button_frame, text="Tính Doanh Thu", width=20, height=2, bg="#98a77c", command=lambda: hien_thi_doanh_thu(HienThi_frame)).pack(padx=20, pady=10, fill='x')

    root.mainloop()


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Nhân Viên
def xoa_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Quản Lý Nhân Viên
def hien_thi_nhan_vien(HienThi_frame):
    xoa_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Nhân Viên", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    MaNV = tk.Entry(HienThi_frame)
    TenNV = tk.Entry(HienThi_frame)
    SdtNV = tk.Entry(HienThi_frame)
    Calam = tk.Entry(HienThi_frame)
    TimNV = tk.Entry(HienThi_frame)

    tk.Label(HienThi_frame, text="Mã Nhân Viên:", relief="solid", bd=2).grid(row=1, column=0, pady=5)
    MaNV.grid(row=1, column=1, pady=5)

    tk.Label(HienThi_frame, text="Họ Tên Nhân Viên:", relief="solid", bd=2).grid(row=2, column=0, pady=5)
    TenNV.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Số Điện Thoại:", relief="solid", bd=2).grid(row=3, column=0, pady=5)
    SdtNV.grid(row=3, column=1, pady=5)

    tk.Label(HienThi_frame, text="Nhập Ca Làm:", relief="solid", bd=2).grid(row=4, column=0, pady=5)
    Calam.grid(row=4, column=1, pady=5)

    tk.Label(HienThi_frame, text="Nhập Mã Nhân Viên để tìm:", relief="solid", bd=2).grid(row=5, column=0, pady=5)
    TimNV.grid(row=5, column=1, pady=5)

    danh_sach_nhan_vien_listbox = tk.Listbox(HienThi_frame, width=150, height=20)
    danh_sach_nhan_vien_listbox.grid(row=6, column=0, columnspan=4, pady=10)

    def cap_nhat_danh_sach_nhan_vien(Nhap_Vao=""):
        danh_sach_nhan_vien_listbox.delete(0, tk.END)
        for nhan_vien in danh_sach_nhan_vien:
            thong_tin_nhan_vien = f"Mã NV-: {nhan_vien['Mã Nhân Viên']} | Tên Nhân Viên-: {nhan_vien['Tên Nhân Viên']} | " \
                                  f"SĐT-: {nhan_vien['Số Điện Thoại']} | Ca Làm-: {nhan_vien['Ca Làm']} | Số Lượng Bán-: {nhan_vien['Số Lượng Bán']}"
            if Nhap_Vao.lower() in thong_tin_nhan_vien.lower():
                danh_sach_nhan_vien_listbox.insert(tk.END, thong_tin_nhan_vien)

    def them_nhan_vien():
        if not MaNV.get() or not TenNV.get() or not SdtNV.get() or not Calam.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin nhân viên!")
            return
        danh_sach_nhan_vien.append({
            "Mã Nhân Viên": MaNV.get(),
            "Tên Nhân Viên": TenNV.get(),
            "Số Điện Thoại": SdtNV.get(),
            "Ca Làm": Calam.get(),
            "Số Lượng Bán": 0})
        cap_nhat_danh_sach_nhan_vien()
        MaNV.delete(0, tk.END)
        TenNV.delete(0, tk.END)
        SdtNV.delete(0, tk.END)
        Calam.delete(0, tk.END)
        messagebox.showinfo("Thành Công", "Nhân Viên đã được thêm!")

    def xoa_nhan_vien():
        nv_chon_xoa = danh_sach_nhan_vien_listbox.curselection()
        if nv_chon_xoa:
            nhan_vien_cho_chon = danh_sach_nhan_vien[nv_chon_xoa[0]]
            danh_sach_nhan_vien.remove(nhan_vien_cho_chon)
            cap_nhat_danh_sach_nhan_vien()
            messagebox.showinfo("Thành Công", "Nhân viên đã được xóa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để xóa!")

    def sua_nhan_vien():
        nv_chon_sua = danh_sach_nhan_vien_listbox.curselection()
        if  nv_chon_sua:
            nhan_vien_cho_chon = danh_sach_nhan_vien[ nv_chon_sua[0]]
            nhan_vien_cho_chon['Mã Nhân Viên'] = MaNV.get()
            nhan_vien_cho_chon['Tên Nhân Viên'] = TenNV.get()
            nhan_vien_cho_chon['Số Điện Thoại'] = SdtNV.get()
            nhan_vien_cho_chon['Ca Làm'] = Calam.get()
            cap_nhat_danh_sach_nhan_vien()
            messagebox.showinfo("Thành Công", "Nhân viên đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để sửa!")

    def tim_kiem_nhan_vien():
        Tim_NV = TimNV.get()  # Lấy mã nhân viên từ ô nhập liệu
        danh_sach_nhan_vien_khop = [nhan_vien for nhan_vien in danh_sach_nhan_vien if
                                    Tim_NV.lower() in nhan_vien['Mã Nhân Viên'].lower()]

        if not danh_sach_nhan_vien_khop:
            messagebox.showinfo("Thông Báo", "Mã Nhân Viên không tồn tại!")
        else:
            # Xóa danh sách nhân viên cũ
            danh_sach_nhan_vien_listbox.delete(0, tk.END)

            # Thêm danh sách nhân viên khớp tìm kiếm vào danh sách
            for nhan_vien in danh_sach_nhan_vien_khop:
                thong_tin_nhan_vien = f"Mã NV-: {nhan_vien['Mã Nhân Viên']} | Tên Nhân Viên-: {nhan_vien['Tên Nhân Viên']} | " \
                                      f"SĐT-: {nhan_vien['Số Điện Thoại']} | Ca Làm-: {nhan_vien['Ca Làm']} | Số Lượng Bán-: {nhan_vien['Số Lượng Bán']}"
                danh_sach_nhan_vien_listbox.insert(tk.END, thong_tin_nhan_vien)

    def tinh_luong_nhan_vien():
        nv_chon_tl= danh_sach_nhan_vien_listbox.curselection()
        if nv_chon_tl:
            nhan_vien_cho_chon = danh_sach_nhan_vien[nv_chon_tl[0]]
            so_luong_ban = nhan_vien_cho_chon['Số Lượng Bán']
            luong_co_ban = 6000000
            thuong = 400000 if so_luong_ban > 400 else 300000 if so_luong_ban > 300 else 200000 if so_luong_ban > 200 else 100000 if so_luong_ban > 100 else 0
            tong_luong = luong_co_ban + thuong
            messagebox.showinfo("Lương Nhân Viên", f"Lương của {nhan_vien_cho_chon['Tên Nhân Viên']} là: {tong_luong:,} VND")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để tính lương!")

    tk.Button(HienThi_frame, text="Thêm Nhân Viên", command=them_nhan_vien, width=20, height=2, bg="#98a77c").grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Xóa Nhân Viên", command=xoa_nhan_vien, width=20, height=2, bg="#98a77c").grid(row=7, column=1, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Sửa Nhân Viên", command=sua_nhan_vien, width=20, height=2, bg="#98a77c").grid(row=7, column=2, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Tìm Kiếm", command=tim_kiem_nhan_vien, width=20, height=2, bg="#98a77c").grid(row=7, column=3, padx=10, pady=10, sticky="nsew")
    tk.Button(HienThi_frame, text="Tính Lương", command=tinh_luong_nhan_vien, width=20, height=2, bg="#98a77c").grid(row=8, column=0, padx=10, pady=10, sticky="nsew")

    cap_nhat_danh_sach_nhan_vien()


# Thức Uống
def hien_thi_thuc_uong(HienThi_frame):
    xoa_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Thức Uống", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    MaN = tk.Entry(HienThi_frame)
    TenN = tk.Entry(HienThi_frame)
    GiaN = tk.Entry(HienThi_frame)
    TimMaN = tk.Entry(HienThi_frame)

    tk.Label(HienThi_frame, text="Mã Thức Uống:", relief="solid", bd=2).grid(row=1, column=0, pady=5)
    MaN.grid(row=1, column=1, pady=5)

    tk.Label(HienThi_frame, text="Tên Thức Uống:", relief="solid", bd=2).grid(row=2, column=0, pady=5)
    TenN.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Giá Thức Uống (VNĐ):", relief="solid", bd=2).grid(row=3, column=0, pady=5)
    GiaN.grid(row=3, column=1, pady=5)

    tk.Label(HienThi_frame, text="Nhập Mã Thức Uống để Tìm:", relief="solid", bd=2).grid(row=4, column=0, pady=5)
    TimMaN.grid(row=4, column=1, pady=5)

    danh_sach_thuc_uong = tk.Listbox(HienThi_frame, width=150, height=20)
    danh_sach_thuc_uong.grid(row=6, column=0, columnspan=5, pady=10)

    def cap_nhat_danh_sach_thuc_uong():
        danh_sach_thuc_uong.delete(0, tk.END)  # Xóa các mục cũ
        for thuc_uong in drink_list:
            try:

                gia_thuc_uong = float(thuc_uong['Giá Thức Uống(VNĐ)'])

                gia_thuc_uong = "{:,.0f}".format(gia_thuc_uong).replace(",", ".")
            except ValueError:

                gia_thuc_uong = "Không hợp lệ"
            danh_sach_thuc_uong.insert(
                tk.END,
                f"Mã Thức Uống: {thuc_uong['Mã Thức Uống']} | Tên Thức Uống: {thuc_uong['Tên Thức Uống']} | Giá Thức Uống: {gia_thuc_uong} VNĐ"
            )

    def them_thuc_uong():
        if not MaN.get() or not TenN.get() or not GiaN.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin thức uống!")
            return
        try:
            int(GiaN.get())  # Kiểm tra giá trị nhập vào là số
        except ValueError:
            messagebox.showerror("Lỗi", "Giá thức uống phải là số!")
            return

        drink_list.append({
            "Mã Thức Uống": MaN.get(),
            "Tên Thức Uống": TenN.get(),
            "Giá Thức Uống(VNĐ)": GiaN.get()
        })
        cap_nhat_danh_sach_thuc_uong()


        MaN.delete(0, tk.END)
        TenN.delete(0, tk.END)
        GiaN.delete(0, tk.END)

        messagebox.showinfo("Thành Công", "Thức Uống đã được thêm!")

    def xoa_thuc_uong():
        selected_index = danh_sach_thuc_uong.curselection()
        if not selected_index:
            messagebox.showerror("Lỗi", "Vui lòng chọn thức uống để xóa!")
            return
        selected_drink = drink_list[selected_index[0]]
        drink_list.remove(selected_drink)
        cap_nhat_danh_sach_thuc_uong()
        messagebox.showinfo("Thành Công", "Thức Uống đã được xóa!")

    def sua_thuc_uong():
        selected_index = danh_sach_thuc_uong.curselection()
        if selected_index:
            selected_drink = drink_list[selected_index[0]]
            selected_drink['Mã Thức Uống'] = MaN.get()
            selected_drink['Tên Thức Uống'] = TenN.get()
            selected_drink['Giá Thức Uống(VNĐ)'] = GiaN.get()
            cap_nhat_danh_sach_thuc_uong()
            messagebox.showinfo("Thành Công", "Thức Uống đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn thức uống để sửa!")

    def tim_kiem_thuc_uong():
        filter_text = TimMaN.get()
        thuc_uong_khop = [thuc_uong for thuc_uong in drink_list if filter_text.lower() in thuc_uong['Mã Thức Uống'].lower()]

        if not thuc_uong_khop:
            messagebox.showinfo("Thông Báo", "Mã Thức Uống không tồn tại!")
        else:
            danh_sach_thuc_uong.delete(0, tk.END)
            for thuc_uong in thuc_uong_khop:
                danh_sach_thuc_uong.insert(tk.END, f"Mã Thức Uống: {thuc_uong['Mã Thức Uống']}| Tên Thức Uống: {thuc_uong['Tên Thức Uống']}")


    tk.Button(HienThi_frame, text="Thêm Thức Uống", command=them_thuc_uong, width=20, height=2, bg="#98a77c").grid(row=8, column=0, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Xóa Thức Uống", command=xoa_thuc_uong, width=20, height=2, bg="#98a77c").grid(row=8, column=1, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Sửa Thức Uống", command=sua_thuc_uong, width=20, height=2, bg="#98a77c").grid(row=8, column=2, padx=10, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Tìm Kiếm Thức Uống", command=tim_kiem_thuc_uong, width=20, height=2, bg="#98a77c").grid(row=8, column=3, padx=10, pady=10, sticky="e")

    cap_nhat_danh_sach_thuc_uong()

# Hoá Đơn
def hien_thi_hoa_don(HienThi_frame):
    clear_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Hoá Đơn", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    ten_khach_hang = tk.Entry(HienThi_frame)
    tk.Label(HienThi_frame, text="Tên Khách Hàng:", relief="solid", bd=2).grid(row=1, column=0, pady=5)
    ten_khach_hang.grid(row=1, column=1, pady=5)

    nhan_vien_combobox = ttk.Combobox(HienThi_frame, values=[nv["Mã Nhân Viên"] for nv in danh_sach_nhan_vien])
    tk.Label(HienThi_frame, text="Chọn Nhân Viên:", relief="solid", bd=2).grid(row=2, column=0, pady=5)
    nhan_vien_combobox.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Chọn Thức Uống:", relief="solid", bd=2).grid(row=3, column=0, pady=5)
    thuc_uong_listbox = tk.Listbox(HienThi_frame, selectmode=tk.MULTIPLE, width=40, height=6)
    thuc_uong_listbox.grid(row=3, column=1, pady=5)
    for tu in drink_list:
        thuc_uong_listbox.insert(tk.END, tu["Tên Thức Uống"])

    tk.Label(HienThi_frame, text="Số Lượng (phân cách bằng dấu phẩy):", relief="solid", bd=2).grid(row=4, column=0, pady=5)
    so_luong_entry = tk.Entry(HienThi_frame)
    so_luong_entry.grid(row=4, column=1, pady=5)

    ngay_hoa_don = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Ngày Lập Hóa Đơn:", relief="solid").grid(row=1, column=2, pady=5)
    ngay_hoa_don.grid(row=2, column=2, pady=5)

    ma_giam_gia = ["GIAM10", "GIAM20", "GIAM30"]
    ma_giam_gia_combobox = ttk.Combobox(HienThi_frame, values=ma_giam_gia)
    ma_giam_gia_combobox.set("Chọn mã giảm giá")
    tk.Label(HienThi_frame, text="Mã Giảm Giá:", relief="solid", bd=2).grid(row=5, column=0, pady=5)
    ma_giam_gia_combobox.grid(row=5, column=1, pady=5)

    danh_sach_hoa_don_listbox = tk.Listbox(HienThi_frame, width=150, height=20)
    danh_sach_hoa_don_listbox.grid(row=6, column=0, columnspan=4, pady=10)

    def cap_nhat_danh_sach_hoa_don():
        danh_sach_hoa_don_listbox.delete(0, tk.END)
        for hoa_don in invoice_list:
            chi_tiet = ", ".join(f"{tu['Thức Uống']} ({tu['Số Lượng']}x {tu['Giá Thức Uống(VNĐ)']:,} VNĐ)" for tu in hoa_don['Chi Tiết Thức Uống'])
            tong_tien_dinh_dang = "{:,.0f}".format(hoa_don['Tổng Tiền']).replace(",", ".")
            danh_sach_hoa_don_listbox.insert(
                tk.END,
                f"Khách Hàng: {hoa_don['Tên Khách Hàng']} | NV: {hoa_don['Nhân Viên']} | "
                f"Thức Uống : {chi_tiet} | Tổng Tiền : {tong_tien_dinh_dang} VNĐ | Giảm Giá: {hoa_don['Giảm Giá']}% |"
                f"Ngày Lập: {hoa_don['Ngày Lập']}"
            )

    def them_hoa_don():
        khach_hang = ten_khach_hang.get()
        nhan_vien = nhan_vien_combobox.get()
        selected_items = thuc_uong_listbox.curselection()
        so_luong_text = so_luong_entry.get()
        ma_giam = ma_giam_gia_combobox.get()
        ngay = ngay_hoa_don.get()

        if khach_hang and nhan_vien and selected_items and so_luong_text:
            try:
                so_luong = list(map(int, so_luong_text.split(',')))
                if len(so_luong) != len(selected_items):
                    messagebox.showerror("Lỗi", "Số lượng không khớp với số món được chọn!")
                    return

                chi_tiet_thuc_uong = []
                tong_tien = 0

                for i, idx in enumerate(selected_items):
                    ten_thuc_uong = thuc_uong_listbox.get(idx)  # Lấy tên thức uống từ Listbox
                    thuc_uong = next((tu for tu in drink_list if tu['Tên Thức Uống'] == ten_thuc_uong), None)
                    if not thuc_uong:
                        continue
                    sl = so_luong[i]
                    gia = int(thuc_uong['Giá Thức Uống(VNĐ)'])
                    tong_tien += sl * gia
                    chi_tiet_thuc_uong.append({
                        "Thức Uống": thuc_uong['Tên Thức Uống'],
                        "Số Lượng": sl,
                        "Giá Thức Uống(VNĐ)": gia
                    })

                giam_gia = int(ma_giam.replace("GIAM", "")) if ma_giam in ma_giam_gia else 0
                tong_tien -= tong_tien * giam_gia / 100

                invoice_list.append({
                    "Tên Khách Hàng": khach_hang,
                    "Nhân Viên": nhan_vien,
                    "Chi Tiết Thức Uống": chi_tiet_thuc_uong,
                    "Tổng Tiền": tong_tien,
                    "Giảm Giá": giam_gia,
                    "Ngày Lập": ngay
                })

                # Cập nhật số lượng bán của nhân viên
                for nv in danh_sach_nhan_vien:
                    if nv['Mã Nhân Viên'] == nhan_vien:
                        nv['Số Lượng Bán'] += sum(so_luong)
                        break

                cap_nhat_danh_sach_hoa_don()
                messagebox.showinfo("Thành Công", "Hóa đơn đã được thêm!")
            except ValueError:
                messagebox.showerror("Lỗi", "Số lượng phải là số và cách nhau bằng dấu phẩy!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin hóa đơn!")

    def xoa_hoa_don():
        chi_so_chon = danh_sach_hoa_don_listbox.curselection()
        if chi_so_chon:
            hoa_don_chon = invoice_list[chi_so_chon[0]]
            invoice_list.remove(hoa_don_chon)
            cap_nhat_danh_sach_hoa_don()
            messagebox.showinfo("Thành Công", "Hoá đơn đã được xóa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn hoá đơn để xóa!")

    def sua_hoa_don():
        chi_so_chon = danh_sach_hoa_don_listbox.curselection()
        if chi_so_chon:
            hoa_don_chon = invoice_list[chi_so_chon[0]]
            hoa_don_chon["Tên Khách Hàng"] = ten_khach_hang.get()
            hoa_don_chon["Nhân Viên"] = nhan_vien_combobox.get()
            cap_nhat_danh_sach_hoa_don()
            messagebox.showinfo("Thành Công", "Hoá đơn đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn hoá đơn để sửa!")

    tk.Button(HienThi_frame, text="Thêm Hoá Đơn", command=them_hoa_don, width=35, height=2, bg="#98a77c").grid(row=7, column=0, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Xóa Hoá Đơn", command=xoa_hoa_don, width=35, height=2, bg="#98a77c").grid(row=7, column=1, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Sửa Hoá Đơn", command=sua_hoa_don, width=35, height=2, bg="#98a77c").grid(row=7, column=2, padx=5, pady=10, sticky="e")

    cap_nhat_danh_sach_hoa_don()


# Doanh Thu
def hien_thi_doanh_thu(HienThi_frame):
    clear_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Tính Doanh Thu", font=("Arial", 17, "bold"), fg="#7B68EE", bg="lightyellow",
             relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    ngay_bat_dau = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Chọn Ngày Bắt Đầu:").grid(pady=5)
    ngay_bat_dau.grid(pady=5)

    ngay_ket_thuc = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Chọn Ngày Kết Thúc:").grid(pady=5)
    ngay_ket_thuc.grid(pady=5)

    def tinh_doanh_thu():
        # Get date range from user
        start_date = datetime.strptime(ngay_bat_dau.get(), "%Y-%m-%d")
        end_date = datetime.strptime(ngay_ket_thuc.get(), "%Y-%m-%d")

        # Filter invoices by date range
        tong_tien = sum(hoa_don["Tổng Tiền"] for hoa_don in invoice_list if
                        start_date <= datetime.strptime(hoa_don["Ngày Lập"], "%Y-%m-%d") <= end_date)
        messagebox.showinfo("Doanh Thu", f"Tổng Doanh Thu trong khoảng thời gian: {tong_tien:,} VNĐ")

    tk.Button(HienThi_frame, text="Tính Doanh Thu", command=tinh_doanh_thu, width=20, height=2, bg="#98a77c").grid(
        row=6, column=2, padx=5, pady=10)

main_window()

