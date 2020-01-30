<template>
    <div>
        <div class="detail_size">
            <section>
                <b-tag class="size" v-for="(item, index) in sizes" :key="index">{{item.value}}</b-tag>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Size",
        props: {
            sizes: {
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
    .size {
        width: 40px;
        height: 20px;
        margin: 0 2px;
    }
    .size:hover {
        background: darkgray;
    }
</style>