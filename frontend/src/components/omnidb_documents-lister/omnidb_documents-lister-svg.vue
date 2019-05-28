<template>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      version="1.1"
      x="0px"
      y="0px"
      :width="getWidth()"
      :height="getHeight()"
      :viewBox="'0 0 16 ' + getHeight()"
      :style="'enable-background:new 0 0 ' + getWidth() + ' ' + getHeight() + '; flex: 0 0 ' + getWidth() + ';'"
      xml:space="preserve"
      fill="none"
      class="omnidb_documents-lister_svg"
    >

        <path
          :d="buildPath( 'start' )"
          stroke-width="1"
          stroke="#819ec8"
          :style="getAnimation(0)"
        >
        </path>

        <path
          :d="buildPath( 'end' )"
          stroke-width="1"
          stroke="gray"
          :style="getAnimation(1)"
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
          default: 40
      },

      itemWidth: {
          type: Number,
          default: 80
      }

  },

  data() {
    return {

        childHeight: this.itemHeight,
        transitionDuration: '0.35s'

    }
  },

  methods: {

      getWidth() {

          return this.itemWidth;

      },

      getHeight( ) {

          return this.itemHeight;

      },

      getAxisPos() {

          return ( this.index % 2 == 0 ) ? this.getWidth() / 2 : this.getWidth() / 4;

      },

      buildPath( pathId ) {

          let width = this.getWidth() / 2,
              height = this.getHeight(),
              center = 8,
              middle = height/2,
              axisPos = center - this.getAxisPos(),
              axisNeg = center + width,
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

      },

      getAnimation( order ) {

          let dashArray = this.itemWidth * 2,
              dashOffset = this.itemWidth * 2,
              transitionDelay = this.index + (0.16 * order) + 's',

              animation = 'stroke-dasharray:' + dashArray + ';' +
                          'stroke-dashoffset:' + dashOffset + ';' +
                          'transition-duration:' + this.transitionDuration + ';' +
                          'transition-delay:' + transitionDelay + ';';

          return animation;

      }

  }

}

</script>

<style lang="scss">
  .omnidb_documents-lister_svg {

      path {
          animation-name: dash;
          animation-fill-mode: forwards;

          //stroke-dashoffset: 64;

          @keyframes dash {
              to {
                  stroke-dashoffset: 0;
              }
          }

      }
  }
</style>
