// https://nuxt.com/docs/api/configuration/nuxt-config
import { resolve } from 'path';

export default defineNuxtConfig({
    modules: ['@inkline/plugin/nuxt', '@inkline/plugin/nuxt', '@nuxt/image-edge', '@nuxt/content'],
    content: {},
    inkline: {
        /**
         * @inkline/config
         * @description provides configuration file specific options
         */

        configFile: resolve(process.cwd(), 'inkline.config.ts'),
        extName: '.scss',
        outputDir: resolve(__dirname, '.inkline/css'),

        /**
         * @inkline/inkline
         * @description provides configuration file specific options
         */

        globals: {
            color: 'dark',
            colorMode: 'system',
            colorModeStrategy: 'localStorage',
            componentOptions: {},
            locale: 'en',
            size: '',
            validateOn: ['input', 'blur']
        },

        /**
         * @inkline/plugin
         * @description provides import specific options
         */

        import: {
            mode: 'auto',
            scripts: true,
            styles: true,
            utilities: true
        }
    }
});
