<template>
  <div id="documentation">
    <div class="container">

      <div class="col-12 col-lg-9">

            <template v-for="ct_section in documents">
                <section class="border-top my-4">

                        <h1 class="text-left">
                          {{ct_section.title}}
                        </h1>

                        <div v-html="ct_section.introtext">


                        </div>

                </section>

            </template>

      </div>

    </div>
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
  mounted () {
    this.getDocuments();
  }
}

</script>
