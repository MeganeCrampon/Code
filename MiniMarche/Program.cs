public class Produit
{
    public int Id { get; set; }
    public string Nom { get; set;} = string.Empty;
    public double Prix { get; set;}
}

class Program
{
    static void Main(string[] args) 
    {
        var catalogue = new List<Produit>
        {
            new Produit { Id = 1, Nom = "Pomme", Prix = 0.80 },
            new Produit { Id = 2, Nom = "Banane", Prix = 1.20 },
            new Produit { Id = 3, Nom = "Poire", Prix = 1.10 }
        };

        var panier = new List<Produit>();
            panier.Add(catalogue[0]);
            panier.Add(catalogue[1]);
            panier.Add(catalogue[2]);

        double prixTotal = 0;
            foreach (var p in panier)
            {
                prixTotal += p.Prix;
            }
            if (prixTotal > 20)
            {
                prixTotal = prixTotal * 0.90; // remise de 10%
            }
        Console.WriteLine("Total : " + prixTotal);
    }
}

