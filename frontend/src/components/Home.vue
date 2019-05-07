<template>
  <div>
    <p>Home page</p>
    <b-button @click="getDocumentation">New random number</b-button>
    </hr>


      <template v-for="ct_section in documents">
          <section class="border-top my-4">

                  <div v-html="ct_section.text">


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
  methods: {
    getDocumentation () {
      this.documents = this.getDocuments()
    },
    getDocuments () {
      const path = 'http://localhost:5000/api/getDocumentation'
      axios.get(path)
        .then(response => {
          this.documents = response.data.data.content_sections[0].content
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
