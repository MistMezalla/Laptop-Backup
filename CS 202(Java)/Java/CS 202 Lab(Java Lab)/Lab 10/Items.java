public class Items {
    int itemCode;
    String itemName;
    double unitPrice;
    int stockRemaining;
    int itemLimit;


    public Items(int itemCode, String itemName, double unitPrice, int stockRemaining,int itemLimit){
        this.itemCode = itemCode;
        this.itemName = itemName;
        this.unitPrice = unitPrice;
        this.stockRemaining = stockRemaining;
        this.itemLimit = itemLimit;
    }

    @Override
    public String toString() {
        return "Item Code: " + itemCode + ",\nName: " + itemName + ",\nUnit Price: " + unitPrice +
                ",\nStock Remaining: " + stockRemaining + ",\nItem Limit: " + itemLimit + "\n";
    }

}
