using CityBikeApi;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddCors();
var app = builder.Build();
app.UseCors(policy => policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader());

var mesStations = new List<Station>
{
    new Station { Id = 1, Nom = "Gare du Nord", VelosDisponibles = 12, CapaciteMax = 15, EstEnService = true },
    new Station { Id = 2, Nom = "Place de l'Hôtel de Ville", VelosDisponibles = 8, CapaciteMax = 12, EstEnService = true },
    new Station { Id = 3, Nom = "Cirque Jules Verne", VelosDisponibles = 6, CapaciteMax = 7, EstEnService = true}
};

app.MapGet("/api/stations", () => {
    return mesStations;
});

app.MapGet("/api/stations/{id}", (int id) => {
    var stationTrouvee = mesStations.FirstOrDefault(s => s.Id == id);
    return stationTrouvee;
});

app.MapPost("/api/stations/{id}/louer", (int id) => 
{   var stationTrouvee = mesStations.FirstOrDefault(s => s.Id == id);

    if (stationTrouvee == null) {
        return Results.NotFound("Cette station n'existe pas.");
    }
    if (stationTrouvee.VelosDisponibles > 0 && stationTrouvee.EstEnService) {
        stationTrouvee.VelosDisponibles--;
        return Results.Ok($"Velo loué ! Il en reste {stationTrouvee.VelosDisponibles}.");
    }
    else {
        return Results.BadRequest("Action impossible : Plus de vélos ou station hors service.");
    }
});

app.MapPost("/api/stations/{id}/rendre", (int id) =>
{
    var stationTrouvee = mesStations.FirstOrDefault(s => s.Id == id);
    if (stationTrouvee == null) {
        return Results.NotFound("Cette station n'existe pas.");
    }
    if (stationTrouvee.EstEnService && stationTrouvee.VelosDisponibles < stationTrouvee.CapaciteMax) {
        stationTrouvee.VelosDisponibles++;
        return Results.Ok($"Velo rendu ! Il en reste {stationTrouvee.VelosDisponibles}.");
    }
    else {
        return Results.BadRequest("Impossible de rendre le vélo : Station hors service ou déjà pleine.");
    }
});

app.MapPost("/api/stations/{id}/toggle", (int id) => 
{   
    var station = mesStations.FirstOrDefault(s => s.Id == id);
    if (station == null)
    {
        return Results.NotFound();
    }
    station.EstEnService = !station.EstEnService;
    return Results.Ok(station);
});

app.UseCors();
app.Run();