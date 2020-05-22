<template>
    <div class="selector">
        <label>
            <select v-model="selected" v-bind:style="{width: width + 'px', height: height + 'px'}" v-on:change="get(selected)">
                <option v-for="(item, index) in items" :key="index" :value="index">
                    {{item.value}}
                </option>
            </select>
        </label>
    </div>
</template>

<script>
    export default {
        name: "Selector",
        props: {
            items: {
                type: Array,
                required: true
            },
            width: {
                type: Number,
                required: false,
                default: 40
            },
            height: {
                type: Number,
                required: false,
                default: 20
            },
            styles: {
                type: Object,
                required: false
            }
        },
        data() {
            return {
                //i18n https://blog.csdn.net/u010987039/article/details/81671886 速查表
                selected: 0,
            }
        },
        methods: {
            get(index) {
                this.$emit('get', this.items[index]);
            }
        }
    }
</script>

<style scoped>
    .selector select {
        box-shadow: none;
        outline: none;
        border: none;
        text-align: center;
        font-family: monospace;
        line-height: 1rem;
        background: black;
        color: white;
    }
</style>