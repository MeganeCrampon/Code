namespace SiteLocaVelos.Models
{
    public class Utilisateur
    {
        public int Id { get; set; }
        public int Nom { get; }
        public string Email { get; } = string.Empty;
        public int Mdp { get;}
        public int DateInscrip { get;}       
    }
}