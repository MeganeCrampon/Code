namespace CityBikeApi;
public class Station {
    public int Id { get; set; }
    public string Nom { get; set; } = string.Empty;
    public int VelosDisponibles { get; set; }
    public bool EstEnService { get; set; } = true;
    public int CapaciteMax { get; set; }
}


