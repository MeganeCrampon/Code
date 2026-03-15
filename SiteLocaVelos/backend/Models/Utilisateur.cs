namespace SiteLocaVelos.Models
{
    public class Utilisateur
    {
        public int Id { get; set; }
        public string Nom { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public string Mdp { get; set; } = string.Empty;
        public DateTime DateInscrip { get; set; } = DateTime.Now;       
    }
}