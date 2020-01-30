<template>
    <div>
        <div v-bind:style="{'float': 'left', 'width': '50%'}">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Images.main_front[language]}}</span>
                </i-col>
            </Row>
            <div class="upload_list front" v-for="item in front.items" :key="item.uid">
                <template v-if="item.status === 'finished'">
                    <img :src="item.url">
                    <div class="upload_list_cover">
                        <Icon type="ios-eye-outline"></Icon>
                        <Icon type="ios-trash-outline" @click="handleFrontDelete(item)"></Icon>
                    </div>
                </template>
                <template v-else>
                    <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                </template>
            </div>
            <Upload
                    v-if="front.items.length < front.max"
                    :show-upload-list="false"
                    :format="['jpg','jpeg','png']"
                    :max-size="maxSize"
                    :on-progress="handleFrontUpload"
                    :on-success="uploadFrontSuccess"
                    multiple
                    type="drag"
                    :action="uri"
                    style="display: inline-block;width:128px;">
                <div style="width: 128px;height:128px;line-height: 128px;">
                    <Icon type="ios-camera" size="128"></Icon>
                </div>
            </Upload>
        </div>
        <div v-bind:style="{'float': 'left', 'width': '50%'}">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Images.main_back[language]}}</span>
                </i-col>
            </Row>
            <div class="upload_list back" v-for="item in back.items" :key="item.uid">
                <template v-if="item.status === 'finished'">
                    <img :src="item.url">
                    <div class="upload_list_cover">
                        <Icon type="ios-eye-outline"></Icon>
                        <Icon type="ios-trash-outline" @click="handleBackDelete(item)"></Icon>
                    </div>
                </template>
                <template v-else>
                    <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                </template>
            </div>
            <Upload
                    v-if="back.items.length < back.max"
                    :show-upload-list="false"
                    :format="['jpg','jpeg','png']"
                    :max-size="maxSize"
                    :on-progress="handleBackUpload"
                    :on-success="uploadBackSuccess"
                    multiple
                    type="drag"
                    :action="uri"
                    style="display: inline-block;width:128px;">
                <div style="width: 128px;height:128px;line-height: 128px;">
                    <Icon type="ios-camera" size="128"></Icon>
                </div>
            </Upload>
        </div>
        <div v-bind:style="{'float': 'left', 'width': '100%'}">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Images.minor[language]}}</span>
                </i-col>
            </Row>
            <div class="upload_list slide" v-for="item in slide.items" :key="item.uid">
                <template v-if="item.status === 'finished'">
                    <img :src="item.url">
                    <div class="upload_list_cover">
                        <Icon type="ios-eye-outline"></Icon>
                        <Icon type="ios-trash-outline" @click="handleSlideDelete(item)"></Icon>
                    </div>
                </template>
                <template v-else>
                    <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                </template>
            </div>
            <Upload
                    v-if="slide.items.length < slide.max"
                    :show-upload-list="false"
                    :format="['jpg','jpeg','png']"
                    :max-size="maxSize"
                    :on-progress="handleSlideUpload"
                    :on-success="uploadSlideSuccess"
                    multiple
                    type="drag"
                    :action="uri"
                    style="display: inline-block;width:96px;">
                <div style="width: 96px;height:96px;line-height: 96px;">
                    <Icon type="ios-camera" size="96"></Icon>
                </div>
            </Upload>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Images",
        props: {
            language: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                languages: this.$languages,
                uri: "//localhost:13147/v1/images",
                domain: "//localhost:13147/",
                maxSize: 2048,
                slide: {
                    items: [],
                    max: 6,
                    direction: 2,
                },
                front: {
                    items: [],
                    max: 1,
                    direction: 1,
                },
                back: {
                    items: [],
                    max: 1,
                    direction: -1,
                },
                data: []
            }
        },
        methods: {
            handleFrontUpload: function(event, file, fileList) {
                this.front.items = fileList;
            },
            handleFrontDelete: function(file) {
                this.front.items.splice(this.front.items.indexOf(file), 1);
                this.Emit();
            },
            uploadFrontSuccess (res, file) {
                file.url =  this.domain + res.uri;
                file.name = res.name;
                file.uri  = res.uri;
                this.Emit();
            },
            handleBackUpload: function(event, file, fileList) {
                this.back.items = fileList;
            },
            handleBackDelete: function(file) {
                this.back.items.splice(this.back.items.indexOf(file), 1);
                this.Emit();
            },
            uploadBackSuccess (res, file) {
                file.url =  this.domain + res.uri;
                file.name = res.name;
                file.uri  = res.uri;
                this.Emit();
            },
            handleSlideUpload: function(event, file, fileList) {
                this.slide.items = fileList;
            },
            handleSlideDelete: function(file) {
                this.slide.items.splice(this.slide.items.indexOf(file), 1);
                this.Emit();
            },
            uploadSlideSuccess (res, file) {
                file.url =  this.domain + res.uri;
                file.name = res.name;
                file.uri  = res.uri;
                this.Emit();
            },
            Emit: function () {
                this.data = [];
                for (let i = 0; i < this.front.items.length; i++) {
                    let value = {};
                    value.url = this.front.items[i].uri;
                    value.direction = this.front.direction;
                    value.sequence  = i;
                    this.data.push(value);
                }
                for (let i = 0; i < this.back.items.length; i++) {
                    let value = {};
                    value.url = this.back.items[i].uri;
                    value.direction = this.back.direction;
                    value.sequence  = i;
                    this.data.push(value);
                }
                for (let i = 0; i < this.slide.items.length; i++) {
                    let value = {};
                    value.url = this.slide.items[i].uri;
                    value.direction = this.slide.direction;
                    value.sequence  = i;
                    this.data.push(value);

                }
                this.$emit("imagesInfo", this.data);
            }
        }
    }
</script>

<style scoped>
    .upload_list {
        display: inline-block;
        text-align: center;
        border: 1px solid transparent;
        border-radius: 4px;
        overflow: hidden;
        background: #fff;
        position: relative;
        box-shadow: 0 1px 1px rgba(0,0,0,.2);
        margin-right: 4px;
    }
    .front, .back {
        width: 130px;
        height: 130px;
        line-height: 130px;
    }
    .slide {
        width: 96px;
        height: 96px;
        line-height: 96px;
    }
    .upload_list img{
        width: 100%;
        height: 100%;
    }
    .upload_list_cover {
        display: none;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0,0,0,.6);
    }
    .upload_list:hover .upload_list_cover{
        display: block;
    }
    .upload_list_cover i {
        color: #fff;
        font-size: 20px;
        cursor: pointer;
        margin: 0 2px;
    }
</style>