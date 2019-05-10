<template>
  <div>
    <p>Home page</p>
    <b-button @click="getDocuments">New random number</b-button>
    </hr>


      <template v-for="ct_section in documents">
          <section class="border-top my-4">

                  <div v-html="ct_section.introtext">


                  </div>

          </section>

      </template>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      documents: 0
    }
  },
  inject:['EventBus'],
  methods: {
    getDocuments () {
      const path = 'http://localhost:5000/api/getDocumentation'
      axios.get(path)
        .then(response => {
          this.documents = response.data.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {

  }
}

</script>
