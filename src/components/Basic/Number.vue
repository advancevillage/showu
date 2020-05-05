<template>
    <div class="number-group" v-bind:style="{width: width + 'px', height: height +  'px'}">
        <header>
            <p v-if="title.length > 0" v-bind:style="{width: (100 - 6 - 1 - (clear.length * 7) * 100 / width) + '%'}">{{title}}</p>
            <button v-if="clear.length > 0" v-bind:style="{width: ((clear.length * 7) * 100 / width) + '%'}" @click="reset">{{clear}}</button>
        </header>
        <section>
            <b-field>
                <b-slider rounded v-model="values" type="is-dark" size="is-small" :min="min" :max="max" :step="step" v-on:change="get">
                    <b-slider-tick :value="values[left]">{{values[left]}}</b-slider-tick>
                    <b-slider-tick :value="values[right]">{{values[right]}}</b-slider-tick>
                </b-slider>
            </b-field>
        </section>
    </div>
</template>

<script>
    export default {
        name: "Number",
        props: {
            title : {
                type: String,
                required: true
            },
            max: {
                type: Number,
                required: true,
            },
            min: {
                type: Number,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 200,
            },
            height: {
                type: Number,
                required: false,
                default: 100
            },
            clear: {
                type: String,
                required: false,
                default: "clear"
            }
        },
        data() {
            return {
                values: [this.min, this.max],
                step: 10,
                left: 0,
                right: 1,
                symbol: "$"
            }
        },
        methods: {
            reset() {
                this.values = [this.min, this.max];
                this.get();
            },
            get() {
                this.$emit('get', this.values);
            }
        }
    }
</script>

<style scoped>
    .number-group {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        font-family: monospace;
        margin: 2px;
        line-height: 1.5rem;
    }
    .number-group header {
        border-bottom: 1px solid darkgray;
        float: left;
        width: 100%;
    }
    .number-group section {
        float: left;
        width: 90%;
        text-align: center;
        margin: 5%;
    }
    .number-group header > p {
        float: left;
        text-align: left;
        margin: 1%;
    }
    .number-group header > button {
        float: left;
        margin: 2%;
        text-align: center;
        outline: none;
        box-shadow: none;
        text-decoration: underline;
        border: none;
        cursor: pointer;
        color: black;
    }
    .number-group header > button:hover {
        font-weight: bolder;
    }
</style>