<script setup>
// On définit ce que le composant reçoit (comme les propriétés de ta classe C#)
defineProps(['produit'])
defineEmits(['ajouter'])
</script>

<template>
  <div class="produit-card">
    <h3>{{ produit.nom }}</h3>
    <p>Prix : <strong>{{ produit.prix }} €</strong></p>
    <p>Stock : {{ produit.quantiteDispo }}</p>
    
    <button @click="$emit('ajouter', produit)" :disabled="produit.quantiteDispo <= 0">
      {{ produit.quantiteDispo > 0 ? 'Ajouter au panier' : 'Rupture' }}
    </button>
  </div>
</template>

<style scoped>
.produit-card {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 8px;
  text-align: center;
  width: 200px;
}
button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 8px 15px;
  cursor: pointer;
  border-radius: 4px;
}
button:disabled {
  background-color: #999;
}
</style>