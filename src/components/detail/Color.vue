<template>
    <div>
        <div class="detail_color">
            <section>
                <div class="color_warp" v-for="(item, index) in colors" :key="index" >
                    <b-tag class="color" v-bind:style="{'background-color': item.rgb}"></b-tag>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Color",
        props: {
            colors: {
                type: Array,
                required: true,
            },
        },
        data() {
            return {

            }
        }
    }
</script>

<style scoped>
    .detail_color {
        width: 100%;
        height: 100%;
    }
    .color, .color_warp {
        margin: 0;
        padding: 0;
        width: 20px;
        height: 20px;
        border-radius: 100%;
    }
    .color_warp {
        float: left;
        width: 25px;
        height: 25px;
        margin-right: 2px;
    }
    .color {
        margin: 2px
    }
    .color:hover {
        margin: 0;
        width: 25px;
        height: 25px
    }
</style>