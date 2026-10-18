import pandas as pd

def analyze_sales(file_path):
    # 1. Veriyi Oku
    df = pd.read_csv(file_path)
    
    # 2. Toplam Satır Cirosunu Hesapla (Quantity * Unit Price)
    df['total_revenue'] = df['quantity'] * df['unit_price']
    
    # 3. Ürün Bazında Toplulaştır (Aggregation)
    product_summary = df.groupby('product').agg(
        total_quantity=('quantity', 'sum'),
        total_revenue=('total_revenue', 'sum')
    ).reset_index()
    
    # 4. Metrikleri Hesapla
    grand_total_revenue = df['total_revenue'].sum()
    top_selling_by_qty = product_summary.loc[product_summary['total_quantity'].idxmax()]
    top_selling_by_rev = product_summary.loc[product_summary['total_revenue'].idxmax()]
    
    # 5. Raporu Ekrana Yazdır
    print("=" * 45)
    print(" ☕ KAHVE DURAĞI - HAFTALIK SATIŞ ANALİZİ")
    print("=" * 45)
    print(f"\n💵 Toplam Ciro: {grand_total_revenue:,} TL")
    print(f"🔥 En Çok Satılan Ürün (Adet): {top_selling_by_qty['product']} ({top_selling_by_qty['total_quantity']} adet)")
    print(f"🏆 Ciro Şampiyonu Ürün: {top_selling_by_rev['product']} ({top_selling_by_rev['total_revenue']:,} TL)")
    
    print("\n--- ÜRÜN BAZLI ÖZET TABLO ---")
    print(product_summary.to_string(index=False))
    print("=" * 45)

if __name__ == "__main__":
    analyze_sales("sales_data.csv")