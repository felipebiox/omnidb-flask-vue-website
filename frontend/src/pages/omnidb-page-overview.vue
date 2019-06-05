<template>
  <div id="omnidb-overview" class="animated fadeIn">

      <div v-for="(section, index) in this.sections" class="container">

          <section
              :id="'overview_section_' + section.alias"

              v-omnidb-scroll
              attr-scroll-target="page-content"
          >

              <div class="container">

                  <div class="row">

                      <div class="col-5">

                          <h1 v-if="section.title" class="text-right">
                              {{section.title}}
                          </h1>

                          <h2 v-if="section.subtitle" class="text-right">
                              {{section.subtitle}}
                          </h2>

                          <div v-if="section.text" v-html="section.text"></div>

                      </div>

                      <div class="col-7">

                          <div class="overview-img">

                              <div
                                  v-if="section.image"
                                  class="section-image"
                                  :style="'background-image:url(' + section.image + ')'"
                              >
                                Test: <span class="text-primary">{{section.image}}</span>
                              </div>

                              <div v-else>
                                  No image...
                              </div>

                          </div>

                      </div>

                  </div>

              </div>

          </section>

      </div>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      sections: 0
    }
  },
  inject:['EventBus'],
  methods: {

      getOverview () {

        const path = 'http://localhost:5000/api/getOverview';
        const config = {
          method: 'GET',
          mode: 'no-cors',
          headers: {
            'Access-Control-Allow-Origin': 'http://localhost:8080',
            'Access-Control-Allow-Headers': 'Authorization',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
            'Access-Control-Allow-Credentials': true,
            //'Content-Type': 'application/json',
            'Content-Type': 'application/json',
          },
          withCredentials: true,
          //credentials: 'same-origin',
          credentials: true
        }

        axios.get( path, config )
          .then(response => {

              this.sections = response.data.data;

              //this.setStatus();

          })
          .catch(error => {
            console.log(error)
          })
      },

  },
  mounted () {

      this.getOverview();

  }
}

</script>
