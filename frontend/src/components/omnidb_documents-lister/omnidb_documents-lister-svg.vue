<template>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      version="1.1"
      x="0px"
      y="0px"
      width="16"
      :height="getHeight()"
      :viewBox="'0 0 16 ' + getHeight()"
      :style="'enable-background:new 0 0 16 ' + getHeight() + ';'"
      xml:space="preserve"
      fill="none"

    >

        <path
          :d="buildPath( 'start' )"
          stroke-width="1"
          stroke="green"
        >
        </path>

        <path
          :d="buildPath( 'end' )"
          stroke-width="1"
          stroke="gray"
        >
        </path>

    </svg>
</template>

<script>

export default {

  name: 'omnidb-documents-lister-svg',

  props: {

      index: {
          type: Number,
          required: true,
          default: 0
      },

      itemHeight: {
          type: Number,
          default: 16
      }

  },

  data() {
    return {

        childHeight: this.itemHeight

    }
  },

  methods: {

      getHeight( ) {

          return this.itemHeight;

      },

      buildPath( pathId ) {

          let height = this.getHeight(),
              center = 8,
              middle = height/2,
              axisPos = center + 6,
              axisNeg = center - 6,
              bottom = height,

          paths = {

              'start': {

                  pathVector : 'M ' +
                                  center + ' ' + 0 +
                                ' V ' +
                                  middle +
                                ' H ' +
                                  axisPos
              },

              'end': {

                  pathVector : 'M ' +
                                  center + ' ' + middle +
                                ' V ' +
                                  bottom
              }

          };


          return paths[ pathId ].pathVector;

      }

  }

}

</script>
