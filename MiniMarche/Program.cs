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

    // PRODUIT A AJOUTER
    Console.WriteLine("Quel est l'ID du produit que vous souhaitez ajouter au panier ?");
    string inputId = Console.ReadLine();

    if (inputId == "0") break;
    else if (int.TryParse(inputId, out int idChoisi))
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
        { 
            Console.WriteLine($"Désolé, l'ID {idChoisi} n'a pas été trouvé");
            continue;  
        }   

        // QUANTITE A AJOUTER
        Console.WriteLine($"Quelle quantité de {produitTrouve.Nom} voulez vous ajouter ?");
        string inputQuant = Console.ReadLine();

        if (inputQuant == "0")
        {
            Console.WriteLine($"Désolé, vous devez ajouter au moins un exemple au panier.");
        }
        else if (int.TryParse(inputQuant, out int quantChoisi))
        {
            if (quantChoisi > produitTrouve.QuantitéDispo)
            {
                Console.WriteLine($"Désolé, il n'y a que {produitTrouve.QuantiteDispo} articles en stock.");
            }
            else 
            {
                for (int i = 0; i < quantChoisi; i++)
                {
                    panier.Add(produitTrouve);
                }
                Console.WriteLine($"{quantChoisi} {produitTrouve.Nom} a été ajouté au panier");
                produitTrouve.QuantiteDispo -= quantChoisi; // Deduire au stock
            }
        }
    }
};

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