<template>
  <v-container>
    <v-card class="pa-4" max-width="400">
      <v-card-title>Inscription</v-card-title>
      
      <v-form @submit.prevent="handleRegister">
        <v-text-field
          v-model="email"
          label="Email"
          type="email"
          required
        ></v-text-field>
         
        <v-text-field
          v-model="nom"
          label="Nom"
          type="name"
          required
        ></v-text-field>

        <v-text-field
          v-model="mdp"
          label="Mot de passe"
          type="password"
          required
        ></v-text-field>

        <v-btn type="submit" color="primary" block>Valider</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const nom = ref('')
const email = ref('')
const mdp = ref('')

const handleRegister = async () => {
    try {
        const donnees = {
            Nom: nom.value,
            Email: email.value,
            Mdp: mdp.value
            }

    const reponse = await axios.post('http://localhost:5000/api/auth/register', donnees)

    alert("Bravo ! " + reponse.data.message)
    
    } catch (error) {
        console.error("Erreur détaillée :", error)
        alert("Erreur lors de l'inscription.")
    }
}

const handleLogin = async () => {
    try {
        const donnees = {

        }
    }
}
</script>