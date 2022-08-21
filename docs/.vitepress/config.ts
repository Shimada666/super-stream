import { defineConfig } from 'vitepress'

const nav = [
  {
    text: 'API',
    activeMatch: '/api/',
    link: '/api/map'
  }
]

const sidebar = {
  '/api/': [
    {
      text: 'API',
      items: [
        { text: 'map', link: '/api/map' },
        { text: 'count', link: '/api/count' },
        { text: 'distinct', link: '/api/distinct' },
        { text: 'filter', link: '/api/filter' },
        { text: 'flat_map', link: '/api/flat_map' },
        { text: 'for_each', link: '/api/for_each' },
        { text: 'group_by', link: '/api/group_by' },
        { text: 'sorted', link: '/api/sorted' },
        { text: 'sum', link: '/api/sum' },
        { text: 'reduce', link: '/api/reduce' },
        { text: 'any_match', link: '/api/any_match' },
        { text: 'all_match', link: '/api/all_match' },
        { text: 'none_match', link: '/api/none_match' },
        { text: 'find_first', link: '/api/find_first' }
      ]
    }
  ]
}


export default defineConfig({
  title: 'SuperStream',
  lastUpdated: true,
  themeConfig: {
    socialLinks: [
      {
        icon: 'github',
        link: 'https://github.com/Shimada666/super-stream'
      }
    ],
    editLink: {
      pattern: 'https://github.com/shimada666/super-stream/edit/master/docs/:path',
      text: 'Edit this page on GitHub'
    },
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2022-present Shimada666'
    },
    nav,
    sidebar
  },
  vite: {
    build: {

    }
  },
  vue: {
    reactivityTransform: true
  }
})
