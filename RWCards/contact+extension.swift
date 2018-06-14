//
//  contact+extension.swift
//  RWCards
//
//  Created by Dang Quoc Huy on 6/14/18.
//  Copyright © 2018 Raywenderlich. All rights reserved.
//

import Foundation

extension Contact {
  func contactTypeToString() -> String {
    switch type {
    case .speaker:
      return "SPEAKER"
    case .attendant:
      return "ATTENDEE"
    case .volunteer:
      return "VOLUNTEER"
    default:
      return "UNKNOWN"
    }
  }
}
