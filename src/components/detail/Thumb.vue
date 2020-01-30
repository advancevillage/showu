<template>
    <div>
        <section>
            <b-carousel-list
                    v-model="thumb.values"
                    :data="thumbs"
                    :arrow="thumb.arrow"
                    :arrow-hover="thumb.arrowHover"
                    :items-to-list="thumb.perList"
                    :repeat="thumb.repeat"
                    :has-drag="thumb.drag"
                    :has-grayscale="thumb.gray"
                    :has-opacity="thumb.opacity" />
        </section>
    </div>
</template>

<script>
    export default {
        name: "Thumb",
        props: {
            thumbs: {
                type: Array,
                required: true,
            },
        },
        data() {
            return {
                thumb: {
                    arrow: true,
                    arrowHover: true,
                    drag: false,
                    gray: false,
                    opacity: false,
                    values: 1,
                    perList: 1,
                    repeat: true,
                }
            }
        }
    }
</script>

<style scoped>
    .carousel-list > .carousel-slides > .carousel-slide > .image > img {
        width: 200px;
        height: 100px;
    }
</style>