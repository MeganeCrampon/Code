namespace SiteLocaVelos.Models
{
    public class Velo
    {
        public int Id { get; set; }
        public string Type { get; set; } = string.Empty;
        public float Tarif { get; set; }
        public int QuantiteDispo { get; set; }
        public string Description { get; set; } = string.Empty;     
    }
}