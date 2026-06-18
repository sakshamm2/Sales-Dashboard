import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

# Import your reliable processing engine functions
from analytics import fetch_all_sales, get_revenue_by_category, calculate_total_revenue
from db import get_connection

# Set up the professional dark theme UI configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ModernSalesDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window settings - Expanded width for split screen layout
        self.title("Enterprise Sales Analytics & Management Suite")
        self.geometry("1200x720")
        self.configure(fg_color="#111827") # Deep modern charcoal background

        # Primary Split Layout Framework
        self.left_panel = ctk.CTkFrame(self, width=320, fg_color="#1F2937", corner_radius=0)
        self.left_panel.pack(side="left", fill="y")
        self.left_panel.pack_propagate(False)

        self.right_panel = ctk.CTkFrame(self, fg_color="transparent")
        self.right_panel.pack(side="right", fill="both", expand=True)

        # Build UI Elements
        self.build_left_form()
        self.build_right_dashboard()

    # --- LEFT PANEL: DATA ENTRY CONTROL ---
    def build_left_form(self):
        # Form Title
        form_title = ctk.CTkLabel(
            self.left_panel, text="Log New Transaction", 
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#F9FAFB"
        )
        form_title.pack(pady=(40, 30), padx=20, anchor="w")

        # Input: Product Name
        ctk.CTkLabel(self.left_panel, text="PRODUCT NAME", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(padx=20, anchor="w")
        self.entry_prod = ctk.CTkEntry(self.left_panel, placeholder_text="e.g., Ultrawide Monitor", fg_color="#374151", border_color="#4B5563", height=35)
        self.entry_prod.pack(fill="x", padx=20, pady=(5, 15))

        # Input: Category Dropdown
        ctk.CTkLabel(self.left_panel, text="PRODUCT CATEGORY", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(padx=20, anchor="w")
        self.combo_cat = ctk.CTkOptionMenu(self.left_panel, values=["Electronics", "Furniture", "Kitchen", "Office"], fg_color="#374151", button_color="#4B5563", height=35)
        self.combo_cat.pack(fill="x", padx=20, pady=(5, 15))

        # Input: Quantity
        ctk.CTkLabel(self.left_panel, text="QUANTITY SOLD", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(padx=20, anchor="w")
        self.entry_qty = ctk.CTkEntry(self.left_panel, placeholder_text="e.g., 2", fg_color="#374151", border_color="#4B5563", height=35)
        self.entry_qty.pack(fill="x", padx=20, pady=(5, 15))

        # Input: Unit Price
        ctk.CTkLabel(self.left_panel, text="UNIT PRICE ($)", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(padx=20, anchor="w")
        self.entry_price = ctk.CTkEntry(self.left_panel, placeholder_text="e.g., 299.99", fg_color="#374151", border_color="#4B5563", height=35)
        self.entry_price.pack(fill="x", padx=20, pady=(5, 15))

        # Input: Date (Pre-filled to today's current date!)
        ctk.CTkLabel(self.left_panel, text="TRANSACTION DATE", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(padx=20, anchor="w")
        today_str = datetime.date.today().strftime("%Y-%m-%d")
        self.entry_date = ctk.CTkEntry(self.left_panel, fg_color="#374151", border_color="#4B5563", height=35)
        self.entry_date.insert(0, today_str)
        self.entry_date.pack(fill="x", padx=20, pady=(5, 30))

        # Action Submission Button
        self.btn_submit = ctk.CTkButton(
            self.left_panel, text="➕ Commit to Database", 
            font=ctk.CTkFont(weight="bold"), fg_color="#6366F1", hover_color="#4F46E5", 
            height=40, command=self.handle_submit
        )
        self.btn_submit.pack(fill="x", padx=20)

        # Success/Error Messaging Label
        self.lbl_status = ctk.CTkLabel(self.left_panel, text="", font=ctk.CTkFont(size=12))
        self.lbl_status.pack(pady=15)

    # --- RIGHT PANEL: LIVE EXECUTIVE READOUTS ---
    def build_right_dashboard(self):
        # Header Banner
        header = ctk.CTkLabel(
            self.right_panel, text="Real-Time Performance Analytics", 
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"), 
            text_color="#F9FAFB"
        )
        header.pack(pady=(25, 15), padx=40, anchor="w")

        # KPI Metrics Display Bar
        self.metrics_container = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        self.metrics_container.pack(fill="x", padx=40, pady=10)

        # Card A: Total Revenue
        self.rev_card = ctk.CTkFrame(self.metrics_container, fg_color="#1F2937", corner_radius=12, height=90)
        self.rev_card.pack_propagate(False)
        self.rev_card.pack(side="left", expand=True, padx=10)
        ctk.CTkLabel(self.rev_card, text="TOTAL REVENUE", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(pady=(15, 2))
        self.lbl_revenue = ctk.CTkLabel(self.rev_card, text="$0.00", font=ctk.CTkFont(size=20, weight="bold"), text_color="#10B981")
        self.lbl_revenue.pack()

        # Card B: Volume
        self.vol_card = ctk.CTkFrame(self.metrics_container, fg_color="#1F2937", corner_radius=12, height=90)
        self.vol_card.pack_propagate(False)
        self.vol_card.pack(side="left", expand=True, padx=10)
        ctk.CTkLabel(self.vol_card, text="TOTAL ITEMS SOLD", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(pady=(15, 2))
        self.lbl_volume = ctk.CTkLabel(self.vol_card, text="0", font=ctk.CTkFont(size=20, weight="bold"), text_color="#3B82F6")
        self.lbl_volume.pack()

        # Card C: Top Category
        self.cat_card = ctk.CTkFrame(self.metrics_container, fg_color="#1F2937", corner_radius=12, height=90)
        self.cat_card.pack_propagate(False)
        self.cat_card.pack(side="left", expand=True, padx=10)
        ctk.CTkLabel(self.cat_card, text="TOP CATEGORY", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9CA3AF").pack(pady=(15, 2))
        self.lbl_category = ctk.CTkLabel(self.cat_card, text="N/A", font=ctk.CTkFont(size=18, weight="bold"), text_color="#F59E0B")
        self.lbl_category.pack()

        # Visual Plot Viewport Frame
        self.chart_panel = ctk.CTkFrame(self.right_panel, fg_color="#1F2937", corner_radius=16)
        self.chart_panel.pack(fill="both", expand=True, padx=40, pady=(20, 30))

        # Pull initial records and perform calculations
        self.refresh_analytics_display()

    def refresh_analytics_display(self):
        """Queries database, updates summary fields, and completely redraws the visual canvas."""
        # 1. Fetch latest state from back-end data engine
        sales_data = fetch_all_sales()
        category_revenue = get_revenue_by_category(sales_data)
        total_revenue = calculate_total_revenue(sales_data)
        total_items = sum(item['quantity'] for item in sales_data)
        top_cat = max(category_revenue, key=category_revenue.get) if category_revenue else "N/A"

        # 2. Update UI Text Components
        self.lbl_revenue.configure(text=f"${total_revenue:,.2f}")
        self.lbl_volume.configure(text=str(total_items))
        self.lbl_category.configure(text=top_cat)

        # 3. Clear existing chart components inside the canvas frame to safely prevent overlaps
        for widget in self.chart_panel.winfo_children():
            widget.destroy()

        if not category_revenue:
            return

        # 4. Generate & Style New Matplotlib Plot
        fig, ax = plt.subplots(figsize=(7, 4), facecolor="#1F2937")
        ax.set_facecolor("#1F2937")

        categories = list(category_revenue.keys())
        revenues = list(category_revenue.values())
        bars = ax.bar(categories, revenues, color="#6366F1", width=0.4, edgecolor="none")

        ax.set_title("Revenue Distribution Breakdown", color="#E5E7EB", fontsize=13, fontweight="bold", pad=15)
        ax.tick_params(colors="#9CA3AF", labelsize=10, length=0)
        ax.spines['bottom'].set_color('#4B5563')
        for edge in ['top', 'right', 'left']:
            ax.spines[edge].set_visible(False)
        
        ax.yaxis.grid(True, linestyle="--", alpha=0.1, color="#FFFFFF")
        ax.set_axisbelow(True)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 15,
                    f"${height:,.0f}",
                    ha='center', va='bottom', color='#E5E7EB', fontsize=9.5, fontweight="bold")

        # 5. Pack figure object back to screen
        canvas = FigureCanvasTkAgg(fig, master=self.chart_panel)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)
        plt.close(fig) # Closes active configuration threads out of memory

    # --- DATABASE WRITE BACK ACTION HANDLER ---
    def handle_submit(self):
        prod = self.entry_prod.get().strip()
        cat = self.combo_cat.get()
        qty = self.entry_qty.get().strip()
        price = self.entry_price.get().strip()
        date = self.entry_date.get().strip()

        # Input Validation Guard
        if not prod or not qty or not price or not date:
            self.lbl_status.configure(text="❌ Blanks detected! Check inputs.", text_color="#EF4444")
            return

        try:
            qty_int = int(qty)
            price_float = float(price)
            
            # Interact with Server via Connection Bridge
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("USE sales_dashboard;")
            
            insert_query = """
                INSERT INTO sales (product_name, category, quantity, price, sale_date)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (prod, cat, qty_int, price_float, date))
            conn.commit()
            
            cursor.close()
            conn.close()

            # Clean UI Input Fields for next item entry
            self.entry_prod.delete(0, 'end')
            self.entry_qty.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            
            # Status Alert & Hot Refresh
            self.lbl_status.configure(text="✅ Transaction stored successfully!", text_color="#10B981")
            self.refresh_analytics_display()

        except ValueError:
            self.lbl_status.configure(text="❌ Invalid numbers for Qty/Price.", text_color="#EF4444")
        except Exception as err:
            self.lbl_status.configure(text=f"❌ DB Error: {err}", text_color="#EF4444")

if __name__ == "__main__":
    app = ModernSalesDashboard()
    app.mainloop()