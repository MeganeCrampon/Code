namespace SiteLocaVelos.Models
{
    public class Reservation
    {
        public int Id { get; set; }
        public int UserId { get; set; }
        public int VeloId { get; set; }
        public int DateDebut { get; set; }
        public int DateFin { get; set; }    
        public float PrixTotal { get; set; }    
        public bool Statut { get; set; }    
    }
}