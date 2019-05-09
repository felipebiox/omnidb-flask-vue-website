import Vue from 'vue';

const EventBus = new Vue();

let EventBusMixin = {
    provide() {
        const provides = {
            EventBus: EventBus
        };

        return provides;
    },
};
export default EventBusMixin;
