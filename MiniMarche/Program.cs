using System.ComponentModel.Design.Serialization;

var catalogue = new List<Produit>
{
    new Produit { Id = 1, Nom = "Pomme", Prix = 0.80, QuantitéDispo = 15 },
    new Produit { Id = 2, Nom = "Banane", Prix = 1.20, QuantitéDispo = 22 },
    new Produit { Id = 3, Nom = "Poire", Prix = 1.10, QuantitéDispo = 13 }
};

var panier = new List<Produit>();

while (true)
{
    Console.WriteLine("\n--- Catalogue disponible ---");
    foreach (var p in catalogue)
    {
        Console.WriteLine($"{p.Id}: {p.Nom} ({p.Prix}€) - Stock : {p.QuantiteDispo}");
    }

    string input = Console.ReadLine("Quel est l'ID du produit que vous souhaitez ajouter au panier ?");

    if (input == "0") break;

    else if (int.TryParse(input, out int idChoisi))
    {
        // [cite_start] ?
        var produitTrouve = catalogue.Find(p => p.Id == idChoisi);

       /* 
        if (produitTrouve != null)
        {
            panier.Add(produitTrouve);
            Console.WriteLine($"{produitTrouve} a été ajouté au panier.");
        } else
        {
            Console.WriteLine("Désolé, l'ID entré est invalide.");
        }
        */

        if(produitTrouve == null) 
            Console.WriteLine($"Désolé, l'ID {produitTrouve.Id} n'a pas été trouvé");
            return;  

        panier.Add(produitTrouve);
        Console.WriteLine($"{produitTrouve} a été ajouté au panier.");  
    }
}

int prixTotal = 0;
    foreach (var p in panier)
    {
        prixTotal += p.Prix;
    }
    if (prixTotal > 20)
    {
        prixTotal = prixTotal * 0.90; // remise de 10%
    }
Console.WriteLine("Total : " + prixTotal);


