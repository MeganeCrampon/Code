<script setup>
import { ref } from 'vue'
import ProduitItem from './components/ProduitItem.vue' // On importe le moule

// Catalogue
const catalogue = ref([
  { id: 1, nom: "Pomme", prix: 0.80, quantiteDispo: 15 },
  { id: 2, nom: "Banane", prix: 1.20, quantiteDispo: 22 },
  { id: 3, nom: "Poire", prix: 1.10, quantiteDispo: 13 }
])

// Panier vide au départ
const panier = ref([])

// Fonction pour ajouter (ancien WHILE)
const ajouterAuPanier = (produit) => {
  if (produit.quantiteDispo > 0) {
    panier.value.push({ ...produit }) // On ajoute une copie au panier
    produit.quantiteDispo--           // On baisse le stock en direct
  }
}
</script>

<template>
  <main>
    <h1>🍎 Mon Petit Marché Vue.js</h1>

    <div class="catalogue-grid">
      for(item in base de donnee)
      {
      <ProduitItem 
        v-for="p in catalogue" 
        :key="p.id" 
        :produit="p" 
        @ajouter="ajouterAuPanier"
      />
      }
    </div>

    <div class="recap">
      <h2>Mon Panier ({{ panier.length }} articles)</h2>
      <p v-if="panier.length === 0">Le panier est vide.</p>
      <ul>
        <li v-for="(item, index) in panier" :key="index">
          {{ item.nom }} - {{ item.prix }} €
        </li>
      </ul>
    </div>
  </main>
</template>

<style>
.catalogue-grid {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  margin-top: 20px;
}
.recap {
  margin-top: 40px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
}
</style>
