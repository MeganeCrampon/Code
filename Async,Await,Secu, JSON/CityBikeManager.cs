public class Station {
    // L'id de la borne
    public int Id { get; set; }
    // Le nom de la rue
    public string Nom { get; set; }
    // Le nombre de vélos restants
    public int VelosDisponibles { get; set; }
    // Est-ce que la station fonctionne ?
    public bool EstEnService { get; set; }
}

