<template>
    <div>
        <section>
            <b-carousel-list
                    v-model="thumb.values"
                    :data="thumb.items"
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
                    items: [
                        {
                            title: 'Slide 1',
                            image: 'https://picsum.photos/id/0/1230/500'
                        },
                        {
                            title: 'Slide 2',
                            image: 'https://picsum.photos/id/1/1230/500'
                        },
                        {
                            title: 'Slide 3',
                            image: 'https://picsum.photos/id/2/1230/500'
                        },
                        {
                            title: 'Slide 4',
                            image: 'https://picsum.photos/id/3/1230/500'
                        },
                        {
                            title: 'Slide 5',
                            image: 'https://picsum.photos/id/4/1230/500'
                        },
                        {
                            title: 'Slide 6',
                            image: 'https://picsum.photos/id/5/1230/500'
                        },
                        {
                            title: 'Slide 7',
                            image: 'https://picsum.photos/id/6/1230/500'
                        }

                    ]
                }
            }
        }
    }
</script>

<style scoped>

</style>